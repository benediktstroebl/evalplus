Here's a Python script that contains a function called `separate_paren_groups` which accepts a string consisting of multiple groups of parentheses and returns a list of these separated groups. The groups are balanced (every open brace has a matching close brace) and they are not nested within each other. The function ignores any spaces in the input string.
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list as an indication of error
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.extend(current_group)

    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```
This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked, and if it is empty, then an error is assumed as the opening parentheses are not balanced with closing parentheses. Otherwise, the top element of the stack is popped and added to the current group. The current group is maintained separately to store the collected parentheses before they are added to the result list. Finally, the last group, which might be still in the stack or in the current_group list, is added to the result list and returned.