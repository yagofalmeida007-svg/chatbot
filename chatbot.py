 #Importação das Bibliotecas:

import os

from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq



#Informa a  gerada

api_key = 'sua ap' # Substitua pela sua API Key

os.environ['GROQ_API_KEY'] = api_key



#Seleciona o modelo

chat = ChatGroq(model='llama-3.3-70b-versatile')



#Função usada para obter as respostas do Bot

def resposta_bot(mensagens):

    mensagens_modelo = [('system', 'Você é meu primeiro assistete Eve ')]

    mensagens_modelo += mensagens #guarda histórico das mensagens

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



#finalização

print('Muito obrigado por usar a Eve')

print(mensagens)
