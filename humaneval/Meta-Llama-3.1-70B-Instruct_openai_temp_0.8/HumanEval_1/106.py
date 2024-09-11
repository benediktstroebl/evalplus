```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into a list of strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a stack and a list to store the result
    stack = []
    result = []

    # Initialize a string to build the current group
    current_group = ''

    # Iterate over the input string
    for char in paren_string:
        # Add the current character to the current group
        current_group += char

        # If the stack is empty and we encounter an opening parenthesis, push it to the stack
        if not stack and char == '(':
            stack.append(char)
        # If the stack is not empty and we encounter a closing parenthesis, pop the opening parenthesis from the stack
        elif stack and char == ')':
            stack.pop()

        # If the stack is empty after popping, we've finished building a group
        if not stack:
            # Add the current group to the result and reset it
            result.append(current_group)
            current_group = ''

    return result


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```