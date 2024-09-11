```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a separate group of nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []
    groups = []
    temp_group = ''

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            temp_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                temp_group += char
                # If the stack is now empty, it means we've found a complete group
                if not stack:
                    groups.append(temp_group)
                    temp_group = ''
            # If the stack is empty, it means we have a closing parenthesis without a matching opening one
            else:
                # This should not happen if the input string is well-formed, but we'll handle it just in case
                temp_group = ''

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string represents a separate group of nested parentheses. The function uses a stack to keep track of the opening parentheses and iterates over each character in the string to separate the groups.