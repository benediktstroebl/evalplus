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
                tmp = stack.pop()
                current_group.extend(tmp)
                if not stack:
                    result.append(')'.join(current_group))
        else:
            current_group.append(char)

    if stack:
        print("There are unbalanced parentheses!")

    return result
```
The code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, it is checked whether the stack is empty. If it is empty, the current group is considered the last one and is added to the result. If it contains elements, the top element is popped and added to the current group. The groups are then separated and returned as a list.