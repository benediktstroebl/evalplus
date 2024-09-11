```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into separate strings.

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

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an opening parenthesis, increment the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ')':
            nesting_level -= 1

        # If the nesting level is zero, we've found a complete group
        if nesting_level == 0:
            # Add the group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ''

    return groups


# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```