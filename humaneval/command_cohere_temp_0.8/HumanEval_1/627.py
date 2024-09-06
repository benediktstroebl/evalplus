```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = ""
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of nested parens and drains the stack accordingly to yield the separate groups. It handles the edge case where a closing paren lacks a matching opening paren by not popping anything from the stack if the current group cannot be closed.