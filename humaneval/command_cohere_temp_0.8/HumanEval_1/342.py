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
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to collect current balanced parentheses groups. It iterates through the input string, pushing entries onto the stack whenever it encounters an open parenthesis and creating a new group. When it encounters a close parenthesis, it checks if the stack is empty. If true, it appends the close parenthesis to the current group, implying an unbalanced group that should be ignored. Otherwise, it pops the top entry from the stack, appends it to the current group, and checks if the stack is empty again. If true, it means the current group is balanced, and it adds it to the result list. The process continues until the entire string has been processed. As a result, the function returns a list of separate groups of parentheses.