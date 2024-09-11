```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty stack to keep track of opening parentheses
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
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    separated_groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means we have a mismatched closing parenthesis
                raise ValueError("Mismatched closing parenthesis")
        # If the character is not a parenthesis, ignore it

    # If there are any remaining opening parentheses in the stack, it means we have a mismatched opening parenthesis
    if stack:
        raise ValueError("Mismatched opening parenthesis")

    return separated_groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses and a string to build the current group. It iterates over each character in the input string, pushing opening parentheses onto the stack and adding them to the current group. When it encounters a closing parenthesis, it pops the corresponding opening parenthesis from the stack and adds it to the current group. If the stack is empty after popping, it means we've found a complete group, which is added to the list of separated groups. If there are any remaining opening parentheses in the stack at the end, it means we have a mismatched opening parenthesis.