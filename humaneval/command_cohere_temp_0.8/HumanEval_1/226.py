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
                return ['Invalid input! No opening parentheses found to match this closing parenthesis.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code leverages a stack to properly handle nested parentheses, and ensures that each opening parenthesis has a corresponding closing parenthesis. It also handles the edge case where there are more closing parentheses than opening ones.