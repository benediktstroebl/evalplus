```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            top_group = stack.pop()
            if not stack:
                result.append(top_group)
            elif current_group:
                stack.append(current Center)
        else:
            current_group += char
    
    return result
```
This Python script uses a stack to manage parentheses groups. When the script encounters an open parentheses `'('` it pushes the current group onto the stack and starts a new group. When it encounters a close parentheses `')'`, it checks if we have a balanced group. If the stack is empty, the group is unbalanced and we return an error. If the stack contains elements, the script pops a group from the stack, checks if the current group is empty, and if so, appends the popped group to the result list. The process continues until all groups are processed.