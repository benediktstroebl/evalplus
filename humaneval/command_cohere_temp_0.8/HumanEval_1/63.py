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
            current_group = []
        else:
            current_group.append(char)
    
    if not stack and current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. At that point, it checks if an opening parenthesis exists in the stack, and if it does, the current group is appended to that opened group, the stack is popped, and the process continues. If not, the current group is appended to the result list and shall be returned once the program finishes iterating through the input string. The resulting list of strings contains all the separate groups of parentheses found in the input string.