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

The algorithm uses a stack to track open parentheses and a list to assemble the current string of parentheses. When a closing parenthesis is encountered, the stack is checked to determine whether it is part of a nested set of parentheses. If not, the current string is appended to the results list and the stack is popped to begin a new string. If it is part of a nested set, the current string is extended with the top element of the stack, and the stack is popped again when the next open parenthesis is encountered. This ensures that each group of parentheses is treated as a single unit and is not confused with other groups.