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
                result.append(')')
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. Then it checks if the current group is empty, in which case the current closing parenthesis is added to the result as an invalid parenthesis. Otherwise, the stack is popped to obtain the corresponding opening parentheses for the current group, and the group is added to the result. The algorithm continues until the entire string is processed.