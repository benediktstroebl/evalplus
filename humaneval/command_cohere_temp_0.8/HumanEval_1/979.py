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
                result.append(''.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm utilizes a stack to track open parentheses and a separate list to track the current group of parentheses. When a closing parenthesis is encountered, the stack is checked to determine whether it is the end of a group or a nested group. If it is the latter, the last group is popped from the stack, combined with the current group, and stacked again for latter processing. This allows us to correctly handle nested groups as well. The resulting list of strings is returned after all groups are processed.