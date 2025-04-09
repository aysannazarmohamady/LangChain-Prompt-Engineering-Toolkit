# LangChain-Prompt-Engineering-Toolkit

A comprehensive guide and toolkit for creating effective prompts with LangChain - from simple templates to complex conversational flows.

🚀 Features

PromptTemplate - Create dynamic text completion prompts
ChatPromptTemplate - Design multi-turn conversations with various roles
MessagesPlaceholder - Manage conversation history and context injection
15+ practical examples across different use cases
Production-ready code with clear documentation

📋 Table of Contents

Installation
Quick Start
Examples

Text Completion
Chat Templates
Conversation Management


Documentation
Contributing
License

🔧 Installation
bash# Clone the repository
git clone https://github.com/aysannazarmohamady/langchain-prompt-engineering.git
cd langchain-prompt-engineering

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
🚀 Quick Start
pythonfrom langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# Simple text prompt
template = PromptTemplate.from_template("Write a short story about {topic}.")
formatted_prompt = template.format(topic="a robot learning to paint")

# Chat prompt
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="Tell me about {topic}."),
])
📚 Examples
Text Completion
pythonfrom langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("Generate a list of 5 {adjective} names for a {pet}.")
formatted_prompt = template.format(adjective="creative", pet="robot cat")
print(formatted_prompt)
Chat Templates
pythonfrom langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a {role}."),
    HumanMessage(content="Hi, can you help me with {topic}?"),
    AIMessage(content="I'd be happy to help with {topic}!"),
    HumanMessage(content="{question}"),
])

messages = template.invoke({
    "role": "math tutor",
    "topic": "calculus",
    "question": "What is the derivative of x²?"
}).messages
Conversation Management
pythonfrom langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessage(content="{question}"),
])

# Simulate conversation history
history = [
    HumanMessage(content="What's 5 + 2?"),
    AIMessage(content="5 + 2 is 7."),
]

messages = template.invoke({
    "history": history,
    "question": "Now multiply that by 4."
}).messages
📖 Documentation
For detailed documentation, check the notebooks in the notebooks/ directory:

01_prompt_templates_basics.ipynb: Introduction to PromptTemplate
02_chat_prompt_templates.ipynb: Working with ChatPromptTemplate
03_messages_placeholder.ipynb: Managing conversation context

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

⭐ If you find this project useful, please consider giving it a star on GitHub! ⭐
