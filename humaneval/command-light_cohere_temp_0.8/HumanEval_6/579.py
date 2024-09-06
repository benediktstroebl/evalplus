```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    result = []
    opening = False
    for char in paren_string:
        if char == '(' and not opening:
            opening = True
        elif char == ')' and opening:
            stack.append(1)
            opening = False
        elif char == '(' and opening:
            stack.append(3)
            opening = False
        elif char == ')' and not opening:
            stack.pop()
        deepest = stack[-1]
            result.append(deepest)
    return result
    return []
```