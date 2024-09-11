### Solution to Separate Parenthesis Groups

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    groups = []
    # Initialize an empty string to build the current group
    current_group = ""
    # Initialize a counter to keep track of the nesting level
    nesting_level = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an open parenthesis, increase the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a close parenthesis, decrease the nesting level
        elif char == ")":
            nesting_level -= 1
            # If the nesting level is zero, it means we've finished a group
            if nesting_level == 0:
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group
                current_group = ""

    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a simple state machine approach to separate the parenthesis groups. It keeps track of the nesting level of the parentheses and uses this to determine when a group is complete. The script ignores any spaces in the input string and returns a list of strings, each representing a separate group of parentheses.