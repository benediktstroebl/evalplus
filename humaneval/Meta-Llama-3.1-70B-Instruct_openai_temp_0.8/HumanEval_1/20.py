```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separated groups of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separated groups
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
        # If the character is a close parenthesis, decrease the nesting level
        elif char == ')':
            nesting_level -= 1

        # Add the character to the current group
        current_group += char

        # If the nesting level is 0, it means we have a complete group
        if nesting_level == 0:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ''

    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```