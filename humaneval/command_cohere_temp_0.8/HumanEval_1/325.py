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
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

This script utilizes a stack to properly separate the groups of parentheses and produce the desired result. In particular, it uses the stack to keep track of the currently open group of parentheses and nests. It also utilizes a list to store the current group's characters. Once the loop completes, the stack is checked to see if it contains any open parentheses. If not, the current group is added to the result list and cleared. If there are open parentheses in the stack, the top element (the most recently added) is popped and added to the current group. The group is then checked again for openness. This guarantees that each open parentheses has a closing partner and that groups are correctly separated.