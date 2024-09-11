```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string containing multiple groups of nested parentheses into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced nested parentheses.
    """

    # Remove spaces from the input string to ignore them
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize a counter to track the balance of parentheses
    balance = 0

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance counter
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance counter
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance counter reaches zero, it means we've found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""
        # If the character is not a parenthesis, skip it

    # Return the list of separate groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple state machine approach to iterate over the input string, tracking the balance of parentheses and building up the separate groups. It correctly handles groups of different sizes and ignores any spaces in the input string.