Here is a self-contained Python script that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    p = []
    open = False
    for c in s:
        if c == '(' and not open:
            open = True
            p.append(1)
        elif c == ')' and open:
            open = False
            if p:
                stack.append(p)
                p = []
        elif c == ')' and open:
            open = False
        else:
            p.append(c)
    return stack
```
This function uses a stack to store the deepest level of nesting of parentheses. It also uses a structure to keep track of the opening and closing of parentheses.