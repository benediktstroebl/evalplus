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
                result.append('')
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                result.append(''.join(current_group))
                current_group = stack.pop() if stack else []
        else:
            current_group.append(char)
    
    # Handle possible remaining brackets
    while stack:
        result.append(''.join(current_group))
        current_group = stack.pop() if stack else []
    
    return result
```

The algorithm uses a stack to keep track of the currently open brackets and constructs the result accordingly. It's careful to handle cases where closing brackets appear without opening ones, either due to improper input or when handling nested brackets.