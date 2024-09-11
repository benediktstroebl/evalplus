```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates multiple groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
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
        # If the character is an open parenthesis, increase the nesting level
        if char == '(':
            nesting_level += 1
            current_group += char
        # If the character is a close parenthesis, decrease the nesting level
        elif char == ')':
            nesting_level -= 1
            current_group += char
            # If the nesting level is zero, it means we've finished a group
            if nesting_level == 0:
                groups.append(current_group)
                current_group = ''

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```