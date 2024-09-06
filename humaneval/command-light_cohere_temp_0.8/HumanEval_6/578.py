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
                result.append(len)
            stack.remove(stack.pop())
        if c == ')'
            stack.append(0)
        elif c == '(':
            stack.append(len+1)
        elif c == ')':
                stack.append(len)
                continue
    return result
```