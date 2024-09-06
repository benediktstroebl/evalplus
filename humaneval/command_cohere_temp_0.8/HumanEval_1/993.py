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
    
    # Handle the last group
    if not stack:
        result.append(')'.join(current_group))
    else:
        pre_group = stack.pop()
        current_group.extend(pre_group)
        result.append(')'.join(current_group))
    
    return result
```
The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses '(' is encountered, the current group is pushed to the stack and a new group is started. When a closing parentheses ')' is encountered, the stack is checked. If the stack is empty, it means we've reached the end of a group, and the current group is added to the results. If there's a group on the stack, it means this ')' closes a previously opened group, so the contents of the current group and the popped group are combined, and the process continues until the end of the string is reached. The final result is a list of separate groups.