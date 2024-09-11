```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into a list of strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    paren_groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increment the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a close parenthesis, decrement the nesting level
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

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each representing a group of nested parentheses. It uses a simple state machine approach to iterate over the input string and build the groups of parentheses. The `nesting_level` variable keeps track of the current nesting level, and when it reaches zero, it means we've found a complete group of parentheses.