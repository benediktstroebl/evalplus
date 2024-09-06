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
                temp = stack.pop()
                current_group.extend(temp)
            current_group = []
        else:
            current_group.append(char)

    if not stack:
        result.append(')'.join(current_group))
    else:
        while stack:
            temp = stack.pop()
            current_group.extend(temp)
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. It shifts every opening parenthesis to the stack and collects all characters in a current group. When a closing parenthesis is encountered, the stack is checked. If it is empty, the current group is added to the results as it is balanced. If there is at least one element in the stack, the top element is popped and appended to the current group. This goes on until the stack is empty again. The resulting list contains every group separated from the input string.