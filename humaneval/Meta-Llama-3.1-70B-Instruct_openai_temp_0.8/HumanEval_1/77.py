```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses as input.
    It separates those groups into separate strings and returns the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Any spaces in the input string are ignored.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings, each representing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # Add the character to the current group
        current_group += char

        # If the nesting level is zero, it means we've found a complete group
        if nesting_level == 0:
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ""

    # Return the list of separate groups
    return separate_groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```