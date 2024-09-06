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
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    if not stack and current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. At that point, it checks if an enclosing parenthesis is at the top of the stack (in which case it accumulates the nested group into the current group). If not, the current group is appended to the result and the stack is popped to resume the original group. The result is a list of separate parentheses groups.