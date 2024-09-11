```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate strings, each containing a balanced group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize a stack to keep track of opening parentheses
    stack = []

    # Initialize a list to store the separate groups
    groups = []

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
            # If the stack is empty, it means the input string is not properly formatted
            if not stack:
                raise ValueError("Unbalanced parentheses in the input string")
            stack.pop()
            current_group += char

        # If the stack is empty, it means we've found a complete group
        if not stack:
            # Add the current group to the list of groups
            groups.append(current_group)
            # Reset the current group
            current_group = ""

    # If the stack is not empty, it means the input string is not properly formatted
    if stack:
        raise ValueError("Unbalanced parentheses in the input string")

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses and a list to store the separate groups. It iterates over each character in the input string, pushing opening parentheses onto the stack and popping them when corresponding closing parentheses are encountered. If the stack is empty when a closing parenthesis is encountered, it means a complete group has been found, so the current group is added to the list of groups. Finally, the script checks if the stack is empty at the end of the input string to ensure that the input string is properly formatted.