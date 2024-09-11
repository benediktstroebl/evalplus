```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # Add the close parenthesis to the current group
            current_group += char
            # If the current group is balanced (i.e., it starts and ends with a parenthesis), add it to the list of groups
            if current_group.count("(") == current_group.count(")"):
                groups.append(current_group)
                current_group = ""

    # Return the list of separated groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of balanced nested parentheses as input and returns a list of strings where each string represents a separate group of balanced parentheses. The function iterates over the characters in the input string, building the current group of parentheses by adding open and close parentheses to it. When a close parenthesis is encountered, the function checks if the current group is balanced by comparing the counts of open and close parentheses. If the group is balanced, it is added to the list of groups, and the current group is reset. Finally, the function returns the list of separated groups.