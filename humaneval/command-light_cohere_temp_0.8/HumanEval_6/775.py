```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = True
    result = []
    for c in s:
        if opening and c == '(':
            stack.append(1)
            opening = False
        elif not opening and c == ')':
            if stack:
                result.append(stack.pop()
               
            stack)
            opening = True
        elif opening and c == '(':
            stack.append(0)
        opening = True
        elif not opening and c == ')':
            pass
    return result
```