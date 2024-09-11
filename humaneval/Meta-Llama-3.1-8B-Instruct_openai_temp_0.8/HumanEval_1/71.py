```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate groups of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the number of open and close parentheses
    open_count = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the counter
        if char == '(':
            open_count += 1
            current_group += char
        # If the character is a close parenthesis, decrement the counter
        elif char == ')':
            open_count -= 1
            current_group += char
        # If the character is not a parenthesis, skip it
        else:
            continue

        # If the counter is 0, it means we have a complete group
        if open_count == 0:
            # Add the group to the list
            groups.append(current_group)
            # Reset the group and counter
            current_group = ''
            open_count = 0

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups of parentheses. It iterates over the input string, keeping track of the number of open and close parentheses. When it encounters a close parenthesis and the counter is 0, it means a complete group has been found, which is added to the list and reset.