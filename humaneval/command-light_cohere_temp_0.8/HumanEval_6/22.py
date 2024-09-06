Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack or stack[-1] == '()':
                result.append(len)
                stack.append(c)
    if stack[-1] == ')':
                stack.pop()
               for c in [')', ')', '(', ']']:
    return result
```