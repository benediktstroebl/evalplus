```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    level = 0
    for c in s:
        if c == '(':
            stack.append(level)
            level += 1
        elif c == ')':
            level -= 1
            if level < 0:
                raise ValueError("Unmatched closing parenthesis.")
            while stack and level:
                stack.pop()
    finished = True
        if c == '(' and finished:
                return [level]
            continue
        else:
            stack.append(None)
    return []
```