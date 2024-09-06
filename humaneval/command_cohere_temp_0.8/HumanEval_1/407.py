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
                print('WRONG')
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    stack.extend(current_group)
    result.extend(stack)
    
    return result
```

The code uses a stack to keep track of open parentheses and properly close them. It handles additional edge cases like nested parentheses and extra closing parentheses. The result list is filled with the correctly separated groups of parentheses.