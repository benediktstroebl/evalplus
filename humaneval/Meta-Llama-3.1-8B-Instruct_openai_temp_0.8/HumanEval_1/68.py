```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, where each string is a group of balanced parentheses.

    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a stack to keep track of the opening parentheses
    stack = []

    # Iterate over each character in the string
    for char in paren_string:
        # If the character is an opening parenthesis
        if char == "(":
            # Push it onto the stack
            stack.append(char)
            # Add it to the current group
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
            # If the stack is empty, it means we've found a complete group
            if not stack:
                # Add the closing parenthesis to the current group
                current_group += char
                # Add the current group to the list of groups
                groups.append(current_group)
                # Reset the current group
                current_group = ""
            else:
                # Add the closing parenthesis to the current group
                current_group += char

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```