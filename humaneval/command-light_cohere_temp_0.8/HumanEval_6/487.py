```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nested = []
    for c in s:
        if c == "(":
            stack.append(1)
        elif c == ")":
            if not stack or stack[-1] == 1:
                nested.append(1)
            stack.pop()
       left nested.
        else:
            stack.append(c)
    stack.append(1)
    return nested
```