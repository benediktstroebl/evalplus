```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                result.append(0)
            stack.append(0)
        elif stack[-1] == 2:
                stack.append(3)
            else:
                stack.append(stack.pop()
               pop(0))
        else:
            stack.append(c)
    return result
```