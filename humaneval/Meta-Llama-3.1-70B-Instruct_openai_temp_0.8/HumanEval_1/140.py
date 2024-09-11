```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    paren_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an opening parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # If the nesting level is zero, it means we've found a complete group
        if nesting_level == 0:
            # Add the current group to the list of groups
            paren_groups.append(current_group)
            # Reset the current group
            current_group = ""

    return paren_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```