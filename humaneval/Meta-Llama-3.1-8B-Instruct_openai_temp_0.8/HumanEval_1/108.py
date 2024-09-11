```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings
    and returns them as a list. It ignores any spaces in the input string and assumes that the
    groups are balanced and not nested within each other.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a separate group of nested parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    groups = []  # Initialize an empty list to store the separate groups
    group = ""  # Initialize an empty string to build the current group

    for char in paren_string:  # Iterate over each character in the input string
        group += char  # Add the character to the current group
        if char == ")":  # If the character is a closing parenthesis
            groups.append(group)  # Add the current group to the list of groups
            group = ""  # Reset the current group

    return groups  # Return the list of separate groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Expected output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input, removes any spaces, and separates the groups into a list of strings. It iterates over each character in the input string, building the current group until it encounters a closing parenthesis, at which point it adds the current group to the list of groups and resets the current group. Finally, it returns the list of separate groups.