```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize an empty stack to keep track of the current group
    stack = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group and push it onto the stack
        if char == '(':
            current_group += char
            stack.append(char)
        # If the character is a close parenthesis, add it to the current group and pop the corresponding open parenthesis from the stack
        elif char == ')':
            current_group += char
            stack.pop()
            # If the stack is empty after popping, it means we've reached the end of a group
            if not stack:
                # Add the current group to the list of groups and reset the current group
                groups.append(current_group)
                current_group = ''

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```