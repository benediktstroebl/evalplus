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
                result.append(''.join(current_group))
            else:
                temp = stack.pop()
                current_group.extend(temp)
            current_group.append(char)
        else:
            current_group.append(char)
            
    if not stack:
        result.append(''.join(current_group))
    else:
        while stack:
            temp = stack.pop()
            current_group.extend(temp)
        result.append(''.join(current_group))
        
    return result
```

The algorithm utilizes a stack to track nested paren groups and a separate list to store the current group. It iterates through the input string, switching between adding opening parens to the current group and pushing the current group onto the stack. When a closing paren is encountered, the algorithm checks if the stack is empty; if so, the current group is added to the result list; otherwise, the topmost group from the stack is appended to the current group, effectively merging them.

This process effectively flattens the nested parentheses, ignoring any spaces, and ensures proper balancing of braces. The resulting list of strings contains each group of parentheses separated and sorted from the inside out.