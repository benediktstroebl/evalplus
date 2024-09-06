```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    stack = []
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if stack:
                result.append(stack.pop()
               pop().22
              stack = []
        else:
            stack[-1] = stack[-1] + 1
    return result
```