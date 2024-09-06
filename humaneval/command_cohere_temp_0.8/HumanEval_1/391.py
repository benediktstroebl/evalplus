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
                print('There is an extra closing parenthesis.')
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print('There is an extra opening parenthesis.')
        return []
    
    result.append(''.join(current_group))
    
    return result
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a corresponding closing parenthesis. The nested parentheses groups are stored in the stack and returned as a list of strings when the string is consumed.

This approach handles cases with extra opening or closing parentheses and properly manages nested groups. It also maintains a correct order in the resulting list.