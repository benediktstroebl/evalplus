```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if len(stack) == 0:
                out.append(None)
            else:
                stack.pop()
                stack.
        else:
            stack.append(char)
   out.
    return out
return out
```