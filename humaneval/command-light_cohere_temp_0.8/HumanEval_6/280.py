```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    open_paren = False
    for c in parent_string:
        if c == "(" and not open_paren:
            open_paren = True
        stack.append(1)
        if c == ")" and open_paren:
            open_paren = False
            result.append(stack.append(0))
        stack.append(0)
    if c == "(":
            stack.append(2)
        if c == ")":
            stack.append(3)
    result.append(stack.pop())
    depth = stack[-1]
    return [depth, result]
```