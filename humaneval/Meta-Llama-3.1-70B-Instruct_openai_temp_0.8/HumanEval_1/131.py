```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into a list of separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    groups = []
    # Initialize an empty stack to keep track of the parentheses
    stack = []
    # Initialize an empty string to build the current group
    group = ''

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it to the stack
        if char == '(':
            stack.append(char)
        # If the character is a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ')':
            stack.pop()
            # If the stack is empty after popping, it means we've found a complete group
            if not stack:
                # Add the current group to the list of groups
                groups.append(group + char)
                # Reset the current group
                group = ''
            else:
                # If the stack is not empty, add the close parenthesis to the current group
                group += char
        # If the character is not a parenthesis, ignore it (this should never happen since we removed spaces)
        else:
            continue

        # If the character is an open parenthesis, add it to the current group
        if char == '(':
            group += char

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```