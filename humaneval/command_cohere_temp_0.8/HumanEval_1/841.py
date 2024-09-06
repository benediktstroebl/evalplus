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
                    current_group.append(char)
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
            
    return result
```
The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings. When it encounters a closing parenthesis, it checks if it matches the most recent open parenthesis. If so, it removes the open parenthesis and the subsequent closing parenthesis from the stack. If not, it creates a new string to hold the current group of parentheses and adds it to the result. The resulting list of strings is returned as the output.