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
                current_group = stack.pop()
                result.append(''.join(current_group))
        else:
            current_group.append(char)
    
    # Handle the last group
    if not stack:
        result.append('')
    elif not stack[-1]:
        result.append('')
    else:
        stack.pop()
        current_group = stack.pop()
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and correctly close and handle nested groups. It also pays attention to the last piece of the string to ensure that no parentheses are missed. After parsing, it strings together the balanced groups and returns them as a list.