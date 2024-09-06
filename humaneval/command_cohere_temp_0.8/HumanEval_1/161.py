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
                result.append(')'.join(current_group))
            else:
                prev_group = stack.pop()
                current_group.extend(prev_group)
            current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, the current group is pushed to the stack and a new empty group is created. When a close parenthesis `)` is encountered, the stack is checked. If it's empty, the current group is popped and added to the result. If it's not empty, the top element of the stack is merged with the current group. This process continues until all parentheses are processed, and all groups are correctly separated.

The result is then returned as a list of separated string groups.