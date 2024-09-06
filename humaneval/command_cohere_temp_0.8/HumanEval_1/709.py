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
    
    # Deal with the last group
    if not stack:
        result.append(')'.join(current_group))
    else:
        pre_group = stack.pop()
        current_group.extend(pre_group)
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to aggregate the contents of each parentheses group. When a closing parenthesis is encountered, the stack is checked to determine whether it corresponds to an open parenthesis in a separate group or the most recent open parenthesis of the current group. If it is the latter, the current group is appended to the result list and cleared. The stack is then used to restore the previous group if there is at least one, otherwise it is discarded. The algorithm continues until all parentheses are processed. This approach ensures that groups of parentheses are correctly distinguished and handled without nesting.