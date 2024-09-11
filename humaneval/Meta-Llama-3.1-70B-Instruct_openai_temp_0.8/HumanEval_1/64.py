```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack to keep track of the parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack and add it to the current group
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack and add it to the current group
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we've found a complete group, so add it to the result and reset the current group
            if not stack:
                result.append(current_group)
                current_group = ''

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```