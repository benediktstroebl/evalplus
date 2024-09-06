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
                print('UNBALANCED!')
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked to see if it's empty (unbalanced). If not, the top of the stack is appended to the current group and the stack is popped. The current group is added to the result list once all parentheses have been processed. This ensures that all groups are separated and properly balanced.