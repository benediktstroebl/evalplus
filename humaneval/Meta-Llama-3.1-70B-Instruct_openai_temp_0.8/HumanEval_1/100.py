```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    :param paren_string: String containing multiple groups of nested parentheses
    :return: List of separated groups of parentheses
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty stack and an empty current group string
    stack = []
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
            # If the stack is empty, it means we've found a complete group, so add it to the result
            if not stack:
                result.append(current_group)
                current_group = ""

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```