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
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)

    # handle the last group
    if stack:
        result.append(''.join(stack.pop()))

    return result
```
This approach uses a stack to keep track of nested parens groups. When a closing paren is encountered, the stack is checked to determine whether it corresponds to an open paren in the current group, or an outer group. Hence, the final list contains separate groups of parentheses, and the resulting list is returned. 

**NOTE:** The edge case of an unbalanced string (i.e. Not properly nested or closed parentheses) will result in a stack trace. This is due to the use of the stack data structure which relies on balanced and properly nested input.