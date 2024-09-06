```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if len(stack) == 0:
                result.append(3)
            stack.append(0)
        else:
                stack.append(stack.pop()
    clear()
        stack at the deepest level of nesting.
```