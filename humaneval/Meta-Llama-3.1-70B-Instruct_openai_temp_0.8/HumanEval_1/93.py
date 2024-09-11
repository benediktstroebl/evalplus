```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separated group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty stack and an empty group string
    stack = []
    group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack and add it to the group string
        if char == "(":
            stack.append(char)
            group += char
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        # and add the close parenthesis to the group string
        elif char == ")":
            stack.pop()
            group += char
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                groups.append(group)
                group = ""

    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```