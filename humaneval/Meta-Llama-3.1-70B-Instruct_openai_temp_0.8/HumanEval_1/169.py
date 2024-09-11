```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack to store the opening parentheses
    stack = []
    
    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []
    
    # Initialize an empty string to store the current group of parentheses
    current_group = ""
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have a complete group of parentheses
            if not stack:
                paren_groups.append(current_group)
                current_group = ""
    
    return paren_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```