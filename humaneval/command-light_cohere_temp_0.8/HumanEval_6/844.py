```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == "(":
            stack.append(0)
        elif c == ")":
            if stack:
                output.append(stack.pop()
           as the real list of the levels of nesting for parentheses. 
```
Output: [0, 0, 1, 3]