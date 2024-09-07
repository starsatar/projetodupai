
import openai

# Substitua pela sua chave de API
openai.api_key = ''

# Inicializa a lista de mensagens com o contexto inicial
messages = [
    {"role": "system", "content": "Você é um assistente prestativo."}
]

def chat():
    while True:
        # Recebe a entrada do usuário
        input_message = input('Esperando input: ')
        
        # Verifica se o usuário quer encerrar a conversa
        if input_message.lower() == 'fim':
            print("Encerrando a conversa.")
            break

        # Adiciona a mensagem do usuário à lista de mensagens
        messages.append({"role": "user", "content": input_message})

        try:
            # Faz a chamada para a API do ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Certifique-se de usar o modelo correto
                messages=messages,
                temperature=1,
                max_tokens=200
            )

            # Obtém a resposta do modelo
            answer = response.choices[0].message['content']

            # Adiciona a resposta do assistente à lista de mensagens
            messages.append({"role": "assistant", "content": answer})

            # Exibe a resposta
            print("Resposta:", answer)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    chat()
