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
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append((').extend([' + ','.join(map(str,current_group)) + '])')))
        else:
            current_group.append(char)
    
    return result
```

The code leverages a stack to properly manage nested parentheses. It accumulates strings in the `current_group` list when the stack is empty, switching to a string manipulation mindset. When a closing parenthesis is encountered, the stack is checked to determine whether the current group is finished. If so, the group is added to the result list and the stack is popped to continue processing the next layer of parentheses. If not, the contents of the stack are appended to the current group and the process continues. This approach ensures balanced and separate groups.