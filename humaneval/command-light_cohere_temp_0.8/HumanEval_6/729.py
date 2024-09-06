```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(len)
        else:
            if not stack or stack[-1] == '(':
                result.append(c)
                stack.append(')')
   
        if stack:
                stack.pop()
    stack.
    return result

```