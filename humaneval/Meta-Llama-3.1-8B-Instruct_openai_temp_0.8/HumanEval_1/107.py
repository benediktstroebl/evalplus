```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input, 
    separates those groups into separate strings and returns the list of those.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over the input string
    for char in paren_string:

        # If the character is an opening parenthesis, push it to the stack
        if char == '(':
            stack.append(char)
            current_group += char

        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            stack.pop()
            current_group += char

            # If the stack is empty after popping, it means we have found a complete group
            if not stack:
                separated_groups.append(current_group)
                current_group = ''

    return separated_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```