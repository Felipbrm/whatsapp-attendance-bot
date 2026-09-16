from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    
    mensagem_recebida = request.values.get("Body", "").strip().lower()
    
    resposta = MessagingResponse()
    
    if mensagem_recebida in ["oi", "ola", "olá", "menu"]:
        texto = (
            "Olá! Como posso te ajudar hoje?\n\n"
            "1 - Horário de funcionamento\n"
            "2 - Agendar uma reunião\n"
            "3 - Falar com atendente humano"
        )
    elif mensagem_recebida == "1":
        texto = "Nosso atendimento é de segunda a sexta, das 09h às 18h."
    elif mensagem_recebida == "2":
        texto = "Para agendar, envie a data e horário desejados (ex: Amanhã às 14h)."
    elif mensagem_recebida == "3":
        texto = "Aguarde um momento, um de nossos atendentes já vai te responder!"
    else:
        texto = "Opção não reconhecida. Digite *menu* para ver as opções disponíveis."

    resposta.message(texto)
    return str(resposta)

if __name__ == "__main__":
    app.run(port=5000, debug=True)