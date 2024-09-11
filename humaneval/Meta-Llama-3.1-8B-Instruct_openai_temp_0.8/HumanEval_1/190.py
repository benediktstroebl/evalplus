Here is a Python script that uses a stack data structure to solve the problem:
```markdown
# Separate Paren Groups
=====================================

This script takes a string of nested parentheses and separates each group into a separate string.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack to store the parentheses
    stack = []
    # Initialize an empty list to store the groups
    groups = []
    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ")":
            stack.pop()
            current_group += char

        # If the stack is empty, it means we've encountered a complete group
        if not stack:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the open parentheses. When it encounters a close parenthesis, it pops the corresponding open parenthesis from the stack. If the stack is empty when it encounters a close parenthesis, it means we've encountered a complete group, so it adds the current group to the list of groups and resets the current group. At the end, it returns the list of groups.