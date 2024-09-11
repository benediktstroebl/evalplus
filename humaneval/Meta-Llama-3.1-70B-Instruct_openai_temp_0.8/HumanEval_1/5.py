```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separated groups
    paren_groups = []
    
    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                paren_groups.append(current_group)
                current_group = ''
    
    return paren_groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```
This script defines a function `separate_paren_groups` that takes a string of parentheses as input, removes any spaces, and then iterates over the string to separate the groups of parentheses. It uses a stack to keep track of the opening parentheses and builds each group as a string. When a complete group is found (i.e., the stack is empty after popping), it is added to the list of groups. The function returns the list of separated groups.