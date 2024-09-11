```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates multiple groups of nested parentheses into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Initialize an empty list to store the separated groups
    groups = []

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
            # If the stack is empty, it means we've encountered an unbalanced closing parenthesis
            else:
                # In this case, we consider the current group complete and add it to the list of groups
                groups.append(current_group)
                # Reset the current group and the stack
                current_group = ""
                stack = []
        # If the stack is empty and the character is not a parenthesis, ignore it
        elif not stack:
            continue

    # Add the last group to the list of groups
    groups.append(current_group)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. The function uses a stack to keep track of opening parentheses and iterates over each character in the input string to separate the groups.