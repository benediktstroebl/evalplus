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

The algorithm uses a stack to track open parentheses and constructs the result accordingly. It switches between two modes:
1. `current_group`: Collects consecutive parentheses and ignores spaces.
2. `stack`: Tracks open parentheses.

When it encounters a closing parenthesis, it checks whether it has an open counterpart on the stack. If it does, it merges the two groups and continues. If not, it adds the current group to the result, if there's no stack, and resets `current_group` for the next iteration.

The result is a list of strings, each containing a separated parenthesis group.