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
                return ['Invalid input! No opening paren to match this closing one.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        return ['Invalid input! Some opening parentheses are not matched with closing ones.']
    else:
        result.append(''.join(current_group))
        return result
```
The algorithm uses a stack to keep track of nested parentheses groups. When encountering an open parenthesis, it pushes the current group onto the stack and starts a new group. Upon encountering a closing parenthesis, it checks if the stack is empty. If so, there's an unbalanced parenthesis, and it returns an error message. Otherwise, it pops the top group from the stack and appends it to the result list. Finally, if there are any unmatched opening parentheses, it returns an error message. 

This approach ensures that groups of parentheses are correctly separated and balanced, and it supports nested groups.