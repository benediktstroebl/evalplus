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
            current_group = []
        else:
            current_group.append(char)
    
    if not stack:
        result.append(')'.join(current_group))
    else:
        while stack:
            pre_group = stack.pop()
            current_group.extend(pre_group)
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to collect the current string between parentheses. It iterates through the input string, pushing each open parenthesis onto the stack and starting a new group when it encounters a closing parenthesis. If the stack is empty, the current group is added to the result list. The algorithm continues until all parentheses are processed. Finally, it returns the list of separate groups.