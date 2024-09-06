```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 1
    for c in s:
        if c == '(':
            stack.append(opening_level)
        elif c == ')':
            stack.pop()
            opening_level = stack.append(0)
        else:
            stack.append(opening_level)
    return stack
```
Do you need help with anything else?