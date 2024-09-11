```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses in a string into a list of strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of balanced nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the groups
    groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and add it to the current group
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group, so add it to the list and reset the current group
                if not stack:
                    groups.append(current_group)
                    current_group = ''
            else:
                # If the stack is empty, it means there's a closing parenthesis without a corresponding opening parenthesis, so we just ignore it
                pass

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings where each string represents a group of balanced nested parentheses. The function uses a stack to keep track of the opening parentheses and a string to build the current group. It iterates over each character in the input string, pushing opening parentheses to the stack, popping corresponding closing parentheses, and adding them to the current group. When a complete group is found, it's added to the list and the current group is reset. The script also includes a test case to demonstrate the function's behavior.