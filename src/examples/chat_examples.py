"""
Examples of using ChatPromptTemplate in different scenarios.

This module demonstrates various use cases for ChatPromptTemplate
from LangChain, including single-turn chats, multi-turn conversations,
and role-playing scenarios.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json

def pretty_print(data):
    """
    Converts data to JSON and prints it in a pretty format.
    
    Args:
        data: The data to pretty-print (dict, list, or object).
    """
    # Convert objects to dictionaries if necessary
    if not isinstance(data, (dict, list)):
        try:
            data = vars(data)  # Convert object to dictionary
        except TypeError:
            pass  # If vars() fails, treat as-is

    # Convert to JSON and print with indentation
    pretty_json = json.dumps(data, indent=4, default=str)
    print(pretty_json)


def single_turn_chat():
    """
    Demonstrates a single-turn chat with SystemMessage and HumanMessage.
    """
    print("\n=== Single-Turn Chat ===")
    
    # Define a chat prompt template
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="Tell me a joke about {topic}."),
    ])

    # Invoke the template with a topic
    prompt_value = template.invoke({"topic": "programmers"})
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


def multi_turn_chat():
    """
    Demonstrates a multi-turn chat with system, human, and AI messages.
    """
    print("\n=== Multi-Turn Chat ===")
    
    # Define a multi-turn chat prompt template
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="Hi, my name is {name}."),
        AIMessage(content="Hello, {name}! How can I help you today?"),
        HumanMessage(content="I need help with {task}."),
    ])

    # Invoke the template with name and task
    prompt_value = template.invoke({"name": "Alice", "task": "writing a resume"})
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


def role_playing_chat():
    """
    Demonstrates a role-playing chat scenario.
    """
    print("\n=== Role-Playing Chat ===")
    
    # Define a role-playing chat prompt template
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a {character}. Speak like a {character} would."),
        HumanMessage(content="Tell me about your day."),
    ])

    # Invoke the template with a character
    prompt_value = template.invoke({"character": "pirate"})
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


def customer_support_chat():
    """
    Demonstrates a customer support chat scenario.
    """
    print("\n=== Customer Support Chat ===")
    
    # Define a customer support chat prompt template
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a customer support agent for {company}."),
        HumanMessage(content="Hi, I have an issue with {product}."),
        AIMessage(content="I'm sorry to hear that. Can you describe the issue?"),
        HumanMessage(content="The issue is {issue}."),
    ])

    # Invoke the template with company, product, and issue
    prompt_value = template.invoke({
        "company": "TechCorp", 
        "product": "smartphone",
        "issue": "it won't turn on"
    })
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


def conversation_with_history():
    """
    Demonstrates using MessagesPlaceholder to include conversation history.
    """
    print("\n=== Conversation With History ===")
    
    # Define a chat prompt template with history
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        HumanMessage(content="{question}"),
    ])

    # Simulate a conversation history
    history = [
        HumanMessage(content="What's 5 + 2?"),
        AIMessage(content="5 + 2 is 7."),
    ]

    # Invoke the template with history and a new question
    prompt_value = template.invoke({
        "history": history,
        "question": "Now multiply that by 4."
    })
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


def limited_history_conversation():
    """
    Demonstrates using MessagesPlaceholder with a limit on the number of messages.
    """
    print("\n=== Limited History Conversation ===")
    
    # Define a chat prompt template with limited history
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history", n_messages=2),
        HumanMessage(content="{question}"),
    ])

    # Simulate a longer conversation history
    history = [
        HumanMessage(content="What's 5 + 2?"),
        AIMessage(content="5 + 2 is 7."),
        HumanMessage(content="Now multiply that by 4."),
        AIMessage(content="7 * 4 is 28."),
    ]

    # Invoke the template with the history and a new question
    prompt_value = template.invoke({
        "history": history,
        "question": "What's the square root of that?"
    })
    
    print("Generated messages:")
    for message in prompt_value.messages:
        print(f"- {message.type}: {message.content}")
    
    return prompt_value.messages


if __name__ == "__main__":
    """
    Run all the example functions.
    """
    single_turn_chat()
    multi_turn_chat()
    role_playing_chat()
    customer_support_chat()
    conversation_with_history()
    limited_history_conversation()
