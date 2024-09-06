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
            
            if not stack:
                result.append(')'.join(current_group))
                current_group = []
        else:
            current_group.append(char)
            
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

This script uses a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, it pushes the current group onto the stack and starts a new group. When a close parenthesis `)` is encountered, it checks whether it belongs to the current group or a nested group. If the stack is empty, it means the current group is complete and it adds it to the results list. If there is a group on the stack, it means the `)` is part of a nested group, so it pops the top of the stack and appends its contents to the current group.

The resulting list of strings, representing the balanced parentheses groups, is returned once all groups are processed.