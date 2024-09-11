```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input, 
    separates those groups into separate strings, and returns the list of those.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the results
    result = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add it to the current group
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                # Add the current group to the result list
                result.append(current_group)
                # Reset the current group
                current_group = ""
        # If the character is not a parenthesis, ignore it

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input. It uses a stack to keep track of the opening parentheses and a string to build the current group. When a closing parenthesis is encountered, the corresponding opening parenthesis is popped from the stack and added to the current group. If the stack is empty after popping, it means we have a complete group, which is added to the result list. The function finally returns the list of separate groups.