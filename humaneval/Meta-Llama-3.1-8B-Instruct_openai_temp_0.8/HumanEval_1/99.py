```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into separate strings.

    Args:
    paren_string: A string containing multiple groups of nested parentheses.

    Returns:
    A list of strings, where each string is a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

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
            # If the current group is balanced (i.e., it has equal numbers of opening and closing parentheses)
            if current_group.count("(") == current_group.count(")"):
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group
                current_group = ""

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups of parentheses. The function removes spaces from the input string, iterates over each character, and builds the current group by adding opening and closing parentheses. When a balanced group is detected (i.e., a group with equal numbers of opening and closing parentheses), the group is added to the list of groups and the current group is reset. Finally, the function returns the list of separated groups.