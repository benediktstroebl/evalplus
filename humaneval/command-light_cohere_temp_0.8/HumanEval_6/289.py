```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    opened = False
    result = []

    for char in parent_string:
        if char == "(":
            if opened:
                stack.append(1)
            opened = True
        else:
            stack.append(0)

    if char == ")":
            if not opened:
                return []
            opened = False
            if stack:
                result.append(stack.pop()
                max_level = stack[-1])
                stack.pop()

    start_level = stack[-1]
                if start_level == max_level + 1:
                    stack.append(3)
                else:
                    stack.append(1)

    if not stack:
        return []

    return result
```