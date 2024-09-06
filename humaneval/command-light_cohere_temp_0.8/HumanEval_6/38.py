```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(len)
        elif c == ')':
            if not stack or stack[-1] == '(':
                result.append(len)
                stack.append(c)
   
    return result
```