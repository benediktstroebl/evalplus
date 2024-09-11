```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    separate_groups.append(current_group)
                    current_group = ""
            # If the stack is already empty, ignore the closing parenthesis (it's a mismatch)
        # If the character is not a parenthesis, ignore it

    return separate_groups


# Test the function
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a simple stack-based approach to separate the groups of balanced parentheses in the input string. It iterates over each character in the string, pushing opening parentheses onto the stack and popping corresponding closing parentheses. When it encounters a closing parenthesis and the stack is empty, it means it's found a complete group, which is then added to the list of separate groups.