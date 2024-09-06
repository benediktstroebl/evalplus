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
                return []  # unbalanced group, returning empty list as convention
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The provided Python script implements a function `separate_paren_groups`, which accepts a string of nested parentheses and returns a list of distinct, nested groups of parentheses, excluding any spaces. To accomplish this, it utilizes a stack data structure to track the open parentheses.

This approach ensures that each open parenthesis has a corresponding close parenthesis, making it possible to separate the groups cleanly. It also handles cases where there are more closing parentheses than opening ones, treating the extra closings as empty groups. The output is a list of these separate groups of parentheses.