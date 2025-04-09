"""
Utility functions for working with LangChain prompts.

This module provides helper functions for creating and managing 
different types of prompts and conversation histories.
"""

from typing import List, Dict, Any, Optional, Union
from langchain_core.prompts import (
    PromptTemplate, 
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    FewShotPromptTemplate
)
from langchain_core.messages import (
    SystemMessage, 
    HumanMessage, 
    AIMessage
)


def create_simple_prompt(template_string: str, **kwargs) -> str:
    """
    Create a simple prompt using PromptTemplate.
    
    Args:
        template_string: The template string with variables in {variable} format
        **kwargs: The variables to fill in the template
        
    Returns:
        The formatted prompt string
    """
    template = PromptTemplate.from_template(template_string)
    return template.format(**kwargs)


def create_chat_prompt(
    system_message: str,
    human_message: str,
    variables: Dict[str, Any]
) -> List[Dict]:
    """
    Create a simple chat prompt with a system message and a human message.
    
    Args:
        system_message: The system message template
        human_message: The human message template
        variables: Dictionary of variables to fill in the templates
        
    Returns:
        The formatted messages as a list of dictionaries
    """
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content=system_message),
        HumanMessage(content=human_message),
    ])
    
    prompt_value = template.invoke(variables)
    return prompt_value.messages


def create_conversation_with_history(
    system_message: str,
    history: List[Union[HumanMessage, AIMessage]],
    current_question: str
) -> List[Dict]:
    """
    Create a conversation prompt that includes conversation history.
    
    Args:
        system_message: The system message template
        history: List of previous messages in the conversation
        current_question: The current question from the user
        
    Returns:
        The formatted messages including history
    """
    template = ChatPromptTemplate.from_messages([
        SystemMessage(content=system_message),
        MessagesPlaceholder(variable_name="history"),
        HumanMessage(content="{question}"),
    ])
    
    prompt_value = template.invoke({
        "history": history,
        "question": current_question
    })
    
    return prompt_value.messages


def create_few_shot_prompt(
    examples: List[Dict[str, str]],
    example_template: str,
    prefix: str,
    suffix: str,
    input_variable: str,
    input_value: str
) -> str:
    """
    Create a few-shot prompt with examples.
    
    Args:
        examples: List of example dictionaries
        example_template: Template string for each example
        prefix: Text to put before the examples
        suffix: Text to put after the examples
        input_variable: The name of the input variable
        input_value: The value for the input variable
        
    Returns:
        The formatted few-shot prompt
    """
    example_prompt = PromptTemplate.from_template(example_template)
    
    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=[input_variable],
    )
    
    return few_shot_prompt.format(**{input_variable: input_value})
