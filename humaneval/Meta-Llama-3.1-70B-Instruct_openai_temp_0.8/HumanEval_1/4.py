```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group
    group = ''

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        group += char

        # If the character is an open parenthesis, increment the nesting level
        if char == '(':
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ')':
            nesting_level -= 1

        # If the nesting level is zero, it means we've found a complete group
        if nesting_level == 0:
            # Add the group to the list of groups
            groups.append(group)
            # Reset the current group
            group = ''

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```