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
                current_group.append(char)
                if not stack:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
            
    return result
```
The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings. When it encounters a closing parenthesis, it checks if it matches the most recent open parenthesis. If so, it removes that open parenthesis from the stack and adds the current string to the results. The code also handles cases where there are unbalanced parentheses by ignoring empty strings for those unbalanced groups.