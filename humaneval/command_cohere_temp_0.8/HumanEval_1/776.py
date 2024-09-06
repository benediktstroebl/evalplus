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

The algorithm uses a stack to track open parentheses and constructs the result iteratively. It switches to a new group when it encounters a closing parenthesis and pops the previous stack element, which is the last opened parenthesis, into the current group. The algorithm also handles the edge case where a group may be nested within another group by extending the previous group with the nested group. Finally, the code takes care not to stick spaces in the resulting strings.