```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string and return them as a list of strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separate groups of nested parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    stack = []
    groups = []
    current_group = ''

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    for char in paren_string:
        if char == '(':
            # Start a new group, push the current group to the result list if it's not empty
            if current_group:
                groups.append(current_group)
            stack.append(char)
            current_group = ''
        elif char == ')':
            # Close the current group, pop the corresponding '(' and add the group to the result list
            if stack:
                stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
        else:
            # Add the character to the current group
            current_group += char

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the parentheses and separate the groups. It iterates over the input string, pushing the opening parentheses onto the stack and adding the corresponding closing parentheses to the current group. When an opening parenthesis is encountered and the stack is empty, the current group is added to the result list.