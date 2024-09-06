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
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    #Deal with the last group
    if not stack:
        result.append(')'.join(current_group))
    else:
        temp_group = stack.pop()
        current_group.extend(temp_group)
        result.append(')'.join(current_group))
    
    return result
```

The approach works by using a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the group is appended to the current group if the stack is empty, indicating the start of a new group. If there is a group at the top of the stack, it is appended to the current group and the stack is popped, continuing the process until the end of the string is reached. At the end of the process, any remaining groups on the stack are appended to the current group and added to the result. The resulting list of strings contains all the unique parenthesis groups, properly balanced and separated.