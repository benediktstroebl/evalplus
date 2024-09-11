### Separate Parenthesis Groups
#### Problem Description
Given a string of multiple groups of nested parentheses, separate these groups into individual strings.

#### Solution

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced, non-nested parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing groups of nested parentheses.

    Returns:
    List[str]: List of separated groups of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    current_group = ''

    # Iterate over the input string
    for char in paren_string:
        # If the character is an open parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
            current_group += char
        # If the character is a close parenthesis
        elif char == ')':
            # Pop the corresponding open parenthesis from the stack
            stack.pop()
            # If the stack is empty, it means we've reached the end of a group
            if not stack:
                result.append(current_group + char)
                current_group = ''
            # Otherwise, add the close parenthesis to the current group
            else:
                current_group += char

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of the open parentheses and a current group string to store the parentheses as we iterate through the input string. When we encounter a close parenthesis and the stack is empty, it means we've reached the end of a group, so we add the current group to the result list and reset the current group. Otherwise, we add the close parenthesis to the current group.