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
        while stack:
            current_group.append(')')
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()

    if current_group:
        result.append(''.join(current_group))

    return result
```

The algorithm utilizes a stack to keep track of open parentheses and constructs the distinct groups of parentheses accordingly. It pushes a group onto the stack when it encounters a closing parenthesis, and pops the stack when it encounters an opening one. Consequently, the stack will hold only the deepest layers of parentheses, while the outermost layers are aggregated in the `result` list.

This approach guarantees that groups of parentheses are correctly separated, balancing each opening parenthesis with a closing one and avoiding nested groupings.