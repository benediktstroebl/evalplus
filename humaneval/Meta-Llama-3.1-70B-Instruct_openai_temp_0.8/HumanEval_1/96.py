```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize a list to store the separate groups
    separate_groups = []

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Initialize a temporary string to build the current group
    temp_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ')':
            nesting_level -= 1

        # Add the character to the temporary group
        temp_group += char

        # If the nesting level is zero, it means we have a complete group
        if nesting_level == 0:
            # Add the complete group to the list of separate groups
            separate_groups.append(temp_group)
            # Reset the temporary group
            temp_group = ''

    return separate_groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```