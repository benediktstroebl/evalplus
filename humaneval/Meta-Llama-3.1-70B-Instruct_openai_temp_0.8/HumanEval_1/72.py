```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into a list of strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == '(':
            stack.append(char)
            group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif char == ')':
            stack.pop()
            group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(group)
                group = ''

    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```