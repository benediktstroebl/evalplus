```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opened = False
    for c in s:
        if c == '(' and not opened:
            opened = True
            stack.append(1)
        elif c == ')':
            if len(stack) == 0:
                return []
            closed = stack.pop()
            if opened:
                return [closed]
            opened = False
        elif c == '(':
            stack.append(0)
        else:
            stack[-1] = c
    return stack
```