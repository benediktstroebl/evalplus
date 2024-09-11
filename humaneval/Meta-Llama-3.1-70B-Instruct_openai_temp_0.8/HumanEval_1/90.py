```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an open count to keep track of the current group
    open_count = 0

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increment the open count
        if char == '(':
            open_count += 1
        # If the character is a close parenthesis, decrement the open count
        elif char == ')':
            open_count -= 1

        # Add the character to the current group
        current_group += char

        # If the open count is zero, it means we have a complete group
        if open_count == 0:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ''

    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```