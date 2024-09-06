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
    
    # Deal with the last remaining group
    if stack:
        pre_group = stack.pop()
        current_group.extend(pre_group)
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and collects closed parentheses until it has formed a balanced group. It then adds this group to the result list and starts a new group for any remaining open parentheses. The algorithm works without caring about any nesting levels of parentheses, due to this idea it's easier to track the balance of parentheses rather than their actual structure.