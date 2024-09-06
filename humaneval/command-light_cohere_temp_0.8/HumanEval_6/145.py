```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for t in s:
        if t == '(':
            stack.append(1)
        elif t == ')':
            if stack:
                stack.pop()
            else
                continue
        stack.append(0)
    else:
                stack.append(t)
    return stack
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest level of nesting parentheses. The function uses a stack data structure to keep track of the opening parentheses.