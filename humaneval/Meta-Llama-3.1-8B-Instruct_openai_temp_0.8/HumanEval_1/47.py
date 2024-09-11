```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a group of balanced parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # Add the closing parenthesis to the current group
            current_group += char
            # Add the current group to the list of separate groups
            separate_groups.append(current_group)
            # Reset the current group
            current_group = ""

    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```