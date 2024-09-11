```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a group of nested parentheses.
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # Add the close parenthesis to the current group
            current_group += char
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string represents a group of nested parentheses. It accomplishes this by iterating over the input string and building up the current group of parentheses. When it encounters a close parenthesis, it adds the current group to the list of groups and resets the current group. Finally, it returns the list of groups.