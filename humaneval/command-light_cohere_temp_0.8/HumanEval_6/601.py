```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    result = []

    for char in s:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if stack:
                stack.opening_level -= 1
                stack.
            if stack and opening_level == 0:
                result.append(opening_level)
                opening_level = 0
            stack.

    return result
```