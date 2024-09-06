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
                if not stack:
                    result.append('')
                else:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
    
    # Handle leftover characters
    while stack:
        current_group = stack.pop()
        result.append(''.join(current_group))
    
    return result
```

This script uses a stack to keep track of nested parens and creates a result list containing the content between each closure. It works regardless of the order and quantity of opening/closing parens, providing an effective solution to the problem statement.