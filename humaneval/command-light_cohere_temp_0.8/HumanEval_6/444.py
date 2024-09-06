```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        elif c == ')':
            if stack:
                l = stack.pop()
                l.
                if l <0: stack.append(0)
            else: stack.append(1)
    elif c == '(': stack.append(2)
        elif c == ')':
                if stack:
                    l = stack.pop()
                    l
                if l.is:
                    else: stack.append(2)
    return stack
```