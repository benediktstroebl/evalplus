```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, 
    separates the groups into individual strings, and returns them in a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a group of balanced parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    paren_groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Initialize a counter to keep track of the nesting level of the parentheses
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the current character to the current group
        current_group += char

        # If the character is an opening parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a closing parenthesis, decrement the nesting level
        elif char == ")":
            nesting_level -= 1

        # If the nesting level is zero, it means we've found a complete group of parentheses
        if nesting_level == 0:
            # Add the current group to the list of groups
            paren_groups.append(current_group)
            # Reset the current group
            current_group = ""

    return paren_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```