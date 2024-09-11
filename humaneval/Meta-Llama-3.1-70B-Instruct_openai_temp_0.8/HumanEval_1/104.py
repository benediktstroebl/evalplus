```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates multiple groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, where each string is a separate group of parentheses.

    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            stack.pop()

            # If the stack is empty after popping, it means we have a complete group
            if not stack:
                # Add the current group to the result list
                result.append(current_group)
                # Reset the current group
                current_group = ''

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Expected output: ['()', '(())', '(()())']
```