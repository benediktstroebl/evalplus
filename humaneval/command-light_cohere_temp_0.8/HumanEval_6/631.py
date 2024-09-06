```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_parens = {}
    close_parens = {}
    for c in s:
        if c == '(':
            stack.append(c)
            if c == ')':
                if stack:
                    parent = stack.pop()
                   
                    open_parens[parent]
                    stack.append(c)
                if c in open_parens:
                        close_parens[open_parens[c]] = c
                open_parens[c] = None
                stack.append(c)
                else:
                    stack.append(c)
        return stack
```