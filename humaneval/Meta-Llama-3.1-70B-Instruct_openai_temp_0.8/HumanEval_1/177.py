```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    :param paren_string: A string containing multiple groups of nested parentheses
    :return: A list of separate groups as strings
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a list to store the result
    result = []

    # Initialize a stack to keep track of the opening parentheses
    stack = []

    # Initialize a string to build the current group
    current_group = ''

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack
        elif char == ')':
            stack.pop()
            current_group += char
            # If the stack is empty, it means we have found a complete group
            if not stack:
                result.append(current_group)
                current_group = ''

    return result


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```