```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    openings: List[int] = []

    for c in s:
        if c == '(':
            stack.append(1)
            openings.append(len)
       
        elif c == ')':
            stack.pop()
            openings.append(3)

    if len(stack) > 1:
        # Top level is the deepest level of nesting.
        for i in range(1, len(stack)-1):
            stack[i] = min(stack[i], stack[i-1])
        stack.append(0)
    openings.append(0)

    return openings
```