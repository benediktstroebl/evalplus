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
                result.append(')')
            else:
                tmp_group = stack.pop()
                current_group.extend(tmp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm utilizes a stack to keep track of opening parentheses until it encounters a closing parenthesis. At that point, it checks if an open parenthesis is at the top of the stack; if it is, it adds the content of the current group to the stack entry, and pops the stack. If not, it simply pops the top entry from the stack, which corresponds to the closing parenthesis of an already closed group, and adds the collected content of that group to the current group. The final result is a list of the separated groups.