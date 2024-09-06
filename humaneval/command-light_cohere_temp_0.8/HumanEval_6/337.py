```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '(':
                out.append(stack.pop())
               
            top_level = len(stack)
                stack.append(0)
            else:
                stack.append(stack.pop())
                next
    .1])
            else:
                stack.append(0)
        out.append(stack.pop())
   
            return out
return out
```