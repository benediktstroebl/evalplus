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
                    result.append((').extend(current_group)')
                elif not temp_group:
                    stack.pop()
    return result
```

The code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked to determine whether it corresponds to the most recent opening parenthesis. If so, the current group is added to the stack and the stack is popped to finalize the group. If not, the stack is checked for the most recent matching opening parenthesis. This allows the program to correctly separate all groups in a single pass without any recursion.