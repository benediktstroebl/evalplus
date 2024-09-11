```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of multiple groups of nested parentheses as input.
    It separates those groups into separate strings and returns the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    It ignores any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups of parentheses
    paren_groups = []

    # Initialize an empty stack to keep track of the opening parentheses
    stack = []

    # Initialize an empty string to build the current group of parentheses
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack and add it to the current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        # and add it to the current group
        elif char == ")":
            stack.pop()
            current_group += char
            # If the stack is empty after popping, it means we have found a complete group of parentheses
            if not stack:
                paren_groups.append(current_group)
                current_group = ""

    return paren_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```