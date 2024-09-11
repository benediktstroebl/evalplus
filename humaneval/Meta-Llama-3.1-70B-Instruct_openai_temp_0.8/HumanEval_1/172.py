```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a string of nested parentheses into separate groups.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a separate group of parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize a list to store the separate groups of parentheses
    separate_groups = []

    # Initialize a stack to keep track of the parentheses
    stack = []

    # Initialize a temporary string to build each group
    temp_group = ""

    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the temporary group
        temp_group += char

        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ")":
            stack.pop()

        # If the stack is empty, it means we've found a complete group of parentheses
        if not stack:
            # Add the temporary group to the list of separate groups
            separate_groups.append(temp_group)
            # Reset the temporary group
            temp_group = ""

    return separate_groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```