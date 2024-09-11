```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a group of nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables to keep track of the groups and the current group
    groups = []
    current_group = ""
    open_parens = 0

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an open parenthesis, increment the counter
        if char == "(":
            open_parens += 1
        # If the character is a close parenthesis, decrement the counter
        elif char == ")":
            open_parens -= 1

        # Add the character to the current group
        current_group += char

        # If the counter is zero, it means we have a complete group
        if open_parens == 0:
            # Add the group to the list of groups and reset the current group
            groups.append(current_group)
            current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```