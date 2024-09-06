Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(start)
        start = i
    if char == ')':
        if len(stack) == 0:
            return []
        stack.pop()
        value = stack.append(start)
        return value
    start = i + 1
    return []
```