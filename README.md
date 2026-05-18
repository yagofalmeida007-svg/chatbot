Eve Chatbot — Google Colab Edition

👨‍💻 Autor
Desenvolvido por Yago Fernandes de Almeida


📄 Licença
MIT License


Chatbot Inteligente com LangChain + Groq no Google Colab:


Projeto desenvolvido em Python utilizando LangChain e a API da Groq para criação de um chatbot com IA executado diretamente no Google Colab.



📌 Sobre o Projeto

A Eve é uma assistente virtual criada para estudos de:

Inteligência Artificial
Engenharia de Prompt
Integração com LLMs
Desenvolvimento de Chatbots
Uso de APIs de IA

O projeto roda diretamente no navegador utilizando o Google Colab, sem necessidade de configurar ambiente local.

| Tecnologia    | Função                      |
| ------------- | --------------------------- |
| Python        | Linguagem principal         |
| Google Colab  | Ambiente de execução        |
| LangChain     | Orquestração do chatbot     |
| Groq API      | Processamento das respostas |
| Llama 3.3 70B | Modelo de linguagem         |
Como Executar no Google Colab
1️⃣ Instale as bibliotecas


Execute esta célula:
!pip install langchain langchain-groq langchain-core
Adicione sua API Key
import os

api_key = "SUA_API_KEY"

os.environ["GROQ_API_KEY"] = api_key



Código Completo:

#Importação das Bibliotecas
import os

from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq



#Informa a API gerada

api_key = 'SUA_API_KEY' # Substitua pela sua API Key

os.environ['GROQ_API_KEY'] = api_key


#Seleciona o modelo

chat = ChatGroq(model='llama-3.3-70b-versatile')


#Função usada para obter as respostas do Bot

def resposta_bot(mensagens):

    mensagens_modelo = [('system', 'Você é meu primeiro assistente Eve')]

    mensagens_modelo += mensagens

    template = ChatPromptTemplate.from_messages(mensagens_modelo)

    chain = template | chat

    return chain.invoke({}).content


#Interação com o usuário

print('Bem-vindo à Eve')

mensagens = []

while True:

    pergunta = input('Usuário: ')

    if pergunta.lower() == 'x':

        break

    mensagens.append(('user', pergunta))

    resposta = resposta_bot(mensagens)

    mensagens.append(('assistant', resposta))

    print(f'Bot: {resposta}')


#Finalização

print('Muito obrigado por usar a Eve')

Exemplo de Uso:

Bem-vindo à Eve

Usuário: O que é Python?

Bot: Python é uma linguagem de programação...


Para encerrar o chatbot:
Usuário: x


Próximos Passos
 Integração com PDFs
 Memória vetorial
 Interface Streamlit
 Banco de dados
 Deploy online
 Docker
