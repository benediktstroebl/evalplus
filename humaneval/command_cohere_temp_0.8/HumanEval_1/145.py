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

The algorithm uses a stack to track open parentheses and a separate list to track the current group of parentheses. When a closing parenthesis is encountered, the stack is checked to see if it is empty. If it is not empty, the top of the stack is appended to the current group and the stack is popped. If the stack is empty, the current group is popped and added to the result list. The algorithm continues until all parentheses have been processed. 

The resulting list of strings is then returned as the output.