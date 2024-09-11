```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of nested parentheses into different groups of balanced parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, where each string is a group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis, add it to the current group
        elif char == ")":
            current_group += char
            # When a close parenthesis is encountered, it means a group is complete
            # Add the complete group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""
    
    # Return the list of separated groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script reads a string of nested parentheses, removes spaces, and then separates the groups of balanced parentheses into different strings. It iterates over each character in the input string, adding open and close parentheses to a current group. When a close parenthesis is encountered, it means a group is complete and is added to the list of groups. The script then returns this list of groups.