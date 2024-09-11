```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each containing a separate group of parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty stack and a list to store the result
    stack = []
    result = []

    # Initialize an empty string to store the current group of parentheses
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group of parentheses
            if not stack:
                result.append(current_group)
                current_group = ''

    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of parentheses. The function uses a stack to keep track of the open parentheses and a string to build the current group of parentheses. When a complete group of parentheses is found (i.e., the stack is empty after popping a close parenthesis), the group is added to the result list.