```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize variables to store the result and the current group
    result = []
    current_group = ''

    # Initialize counters for open and close parentheses
    open_count = 0
    close_count = 0

    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the open count
        if char == '(':
            open_count += 1
        # If the character is a close parenthesis, increment the close count
        elif char == ')':
            close_count += 1

        # If the open and close counts are equal, it means we've found a complete group
        if open_count == close_count:
            # Add the group to the result and reset the current group and counters
            result.append(current_group)
            current_group = ''
            open_count = 0
            close_count = 0

    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```