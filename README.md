# 🤖 Eve AI Chatbot — LangChain + Groq + Llama 3.3

# 📌 Sobre o Projeto

O **Eve AI Chatbot** é um chatbot desenvolvido em Python utilizando:

- **LangChain**
- **Groq API**
- **Modelo Llama 3.3 70B Versatile**

O projeto foi criado com foco em aprendizado prático de:

✅ Inteligência Artificial  
✅ Engenharia de Prompt  
✅ Integração com APIs  
✅ Estruturação de Chatbots  
✅ Fluxos Conversacionais  
✅ Versionamento com Git/GitHub  

---

# 🚀 Demonstração

```bash
Bem-vindo à Eve

Usuário: oi
Bot: Olá! Como posso ajudar você hoje?

Usuário: quem criou você?
Bot: Fui desenvolvido utilizando Python, LangChain e modelos de IA da Groq.

🧠 Tecnologias Utilizadas
Tecnologia	Finalidade
Python	Linguagem principal
LangChain	Orquestração da IA
Groq API	Processamento do modelo
Llama 3.3 70B	Modelo de linguagem
Google Colab	Ambiente de execução
Git/GitHub	Versionamento
📂 Estrutura do Projeto
eve-chatbot/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── assets/
⚙️ Executando no Google Colab
1️⃣ Instale as dependências
!pip install langchain langchain-core langchain-groq groq
2️⃣ Cole o código no Colab
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# API Key
api_key = 'SUA_API_KEY'

os.environ['GROQ_API_KEY'] = api_key

# Modelo
chat = ChatGroq(
    model='llama-3.3-70b-versatile'
)

# Função principal
def resposta_bot(mensagens):

    mensagens_modelo = [
        ('system', 'Você é meu primeiro assistente Eve')
    ]

    mensagens_modelo += mensagens

    template = ChatPromptTemplate.from_messages(
        mensagens_modelo
    )

    chain = template | chat

    return chain.invoke({}).content

# Chat
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

print('Muito obrigado por usar a Eve')
🔑 Como obter a API Key da Groq
Crie uma conta na Groq
Gere uma API Key
Substitua:
api_key = 'SUA_API_KEY'
💡 Funcionalidades
Chat interativo no terminal
Histórico de mensagens
Integração com IA Generativa
Estrutura pronta para expansão
Fácil adaptação para novos modelos
📈 Diferenciais Técnicos

Este projeto demonstra:

✅ Integração com LLMs modernos
✅ Engenharia de Prompt
✅ Uso de LangChain
✅ Manipulação de histórico conversacional
✅ Estrutura inicial de arquitetura IA
✅ Organização de fluxo conversacional

🛠️ Melhorias Futuras
 Interface Web
 Memória persistente
 Integração com PDF
 Banco de dados
 API REST
 Deploy online
 Interface gráfica
📚 Aprendizados Aplicados

Durante o desenvolvimento foram utilizados conceitos de:

Lógica de Programação
Inteligência Artificial
Estruturação de Prompts
Consumo de APIs
Organização de Projetos
Controle de Fluxo
Versionamento Git
🔥 Valor para Portfólio

Este projeto agrega valor ao GitHub porque demonstra:

🧠 Conhecimentos Técnicos
IA Generativa
APIs de IA
Python moderno
LangChain
🚀 Evolução Contínua
Projeto escalável
Fácil manutenção
Expansão modular
🧩 Versionamento do Projeto

Este projeto utiliza Git para controle de versões.

Exemplo de commits profissionais
feat: adiciona integração com Groq API

fix: corrige histórico de mensagens

docs: atualiza documentação do chatbot

refactor: melhora estrutura da função principal

Padrão utilizado:

Conventional Commits
📦 requirements.txt
langchain
langchain-core
langchain-groq
groq
🚫 .gitignore
__pycache__/
.env
venv/
*.pyc

🤖 Uso de IA no Fluxo de Desenvolvimento

Este projeto faz parte do meu processo de aprendizado em:

Engenharia de Prompt
Estruturação de Chatbots
IA Generativa
Automação de Fluxos
Desenvolvimento Assistido por IA

Utilizo IA como ferramenta de:

Prototipação
Aprendizado acelerado
Estruturação técnica
Otimização de código
👨‍💻 Autor
Yago Fernandes de Almeida

Foco em:

Inteligência Artificial
Engenharia de Prompt
Python
Chatbots
Automação
⭐ Contribuição

Contribuições são bem-vindas.

Faça um Fork
Crie uma Branch
Commit suas alterações
Abra um Pull Request
📄 Licença

Este projeto está sob a licença MIT.

🌟 Próximos Projetos
Chatbot com memória
IA conectada a PDFs
Assistente com voz
Sistema de automação IA
Dashboard para IA
Integração com banco de dados
