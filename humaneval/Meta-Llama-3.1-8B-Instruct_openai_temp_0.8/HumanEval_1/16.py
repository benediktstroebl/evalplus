```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    groups = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            stack.pop()
            current_group += char
            if not stack:
                # If the stack is empty, it means we've found a complete group
                groups.append(current_group)
                current_group = ""
        # Ignore spaces in the input string
        elif char!='':
            current_group += char

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a stack data structure to keep track of the opening and closing parentheses. When a closing parenthesis is encountered and the stack is empty, it means we've found a complete group, so we add it to the list of groups and reset the current group.