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
        temp = stack.pop()
        current_group.extend(temp)
        result.append(')'.join(current_group))

    return result
```

The code leverages a stack to manage the nested parentheses correctly. It avoids the issue of nested lists within the `result` list by temporarily storing the current group in the stack and popping the previous group when a closing parenthesis is encountered. This way, it ensures that only the outermost layers of parentheses are retained in the `result` list.