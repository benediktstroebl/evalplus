```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, separates the groups into individual strings
    and returns them as a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add the closing parenthesis to the current group
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means we have a closing parenthesis without a corresponding opening one
                raise ValueError("Unbalanced parentheses in the input string")

    # If there are any remaining opening parentheses in the stack, it means the input string is unbalanced
    if stack:
        raise ValueError("Unbalanced parentheses in the input string")

    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the opening parentheses and builds the current group as it iterates over the input string. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack and adds the closing parenthesis to the current group. If the stack is empty after popping, it means we've found a complete group, so we add it to the list of groups and reset the current group. If there are any remaining opening parentheses in the stack at the end, it means the input string is unbalanced, so we raise a ValueError.