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

The algorithm uses a stack to keep track of nested parentheses groups. It initializes an empty `result` list and iterates through the input string character by character. When an open parenthesis `(` is encountered, the current group is pushed to the stack and a new empty group is created. When a closing parenthesis `)` is encountered, the algorithm checks if the stack is empty. If it's not, the top group is popped from the stack, appended to the current group, and this process is repeated until the stack is empty. The `result` list is then filled with the separated string groups.