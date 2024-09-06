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
                print('UNBALANCED!)'
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

The code uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to save all other characters. Once a closing parenthesis `)` is encountered, the latest `current_group` is appended to the stack element popped from it, ensuring the group is properly closed. The result is in correct format with balanced groups and without nesting.