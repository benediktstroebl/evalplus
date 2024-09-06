```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(":
            stack.append(1)
        elif char == ")":
            stack.pop()
        if len(stack) == 0:
                result.append(0)
                else:
                result.append(len(stack) + 1)
                stack.append(0)
    else:
                stack.append(char)
    return result
```