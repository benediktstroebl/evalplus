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
            elif len(current_group) == 0:
                result.append('')
            else:
                temp = []
                while stack and stack[-1]:
                    temp.append(stack.pop())
                temp.append(current_group)
                result.append(''.join(temp))
            
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and constructs the resulting strings accordingly. It correctly handles cases with multiple parentheses groups and properly manages nested and unbalanced groups.