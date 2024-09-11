```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize an empty stack and an empty current group
    stack = []
    current_group = ''

    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            stack.pop()

        # If the stack is empty, it means we've found a complete group
        if not stack:
            # Add the complete group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ''

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```