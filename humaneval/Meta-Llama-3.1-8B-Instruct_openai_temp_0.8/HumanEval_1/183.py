```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings and return the list of those.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: List of strings, each containing a separate group of nested parentheses.
    """
    stack = []  # Initialize empty stack to keep track of opening parentheses
    groups = []  # Initialize list to store the separated groups
    current_group = ""  # Initialize variable to store the current group being processed

    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:  # Check if stack is not empty before popping
                stack.pop()
                current_group += char
            # If the stack is empty, it means we've found a complete group, so add it to the list and reset the current group
            else:
                groups.append(current_group)
                current_group = ""
        # If the character is not a parenthesis, ignore it

    # If there are any remaining opening parentheses in the stack, it means there are some incomplete groups at the end of the string
    if stack:
        groups.append(current_group)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input, separates the groups into individual strings, and returns the list of strings. The function uses a stack to keep track of the opening parentheses and a variable to store the current group being processed. The script also includes a test case to demonstrate the function's usage.