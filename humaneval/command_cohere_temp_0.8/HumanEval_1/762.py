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
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the group is appended to the current group if the stack is empty, indicating the outermost group is closed. If there are elements in the stack, the most recent group is popped and appended to the current group. The process ensures that all groups are properly separated and nested within each other. The resulting list of strings contains the separated parenthesis groups.