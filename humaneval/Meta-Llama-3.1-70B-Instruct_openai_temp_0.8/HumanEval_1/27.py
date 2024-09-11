```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into a list of strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty stack to keep track of the current group
    current_group = []

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == '(':
            current_group.append(char)
        # If the character is a close parenthesis, add it to the current group
        elif char == ')':
            current_group.append(char)
            # If the current group is balanced (i.e., it has an equal number of open and close parentheses),
            # add it to the list of separate groups and reset the current group
            if current_group.count('(') == current_group.count(')'):
                separate_groups.append(''.join(current_group))
                current_group = []

    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```