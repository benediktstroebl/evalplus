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
    
    # Handling edge case for unbalanced groups
    if stack:
        result.extend(')'.join(group) for group in stack)
    
    return result
```
The algorithm uses a stack to keep track of opening parentheses and creates a corresponding list of strings, each containing a separate group of parentheses. After popping the stack, the current group is appended to the previous group and added to the results list if the stack is empty. This ensures that all groups are properly separated and nested within each other.