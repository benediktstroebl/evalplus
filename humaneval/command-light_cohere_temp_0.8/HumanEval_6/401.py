```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if stack:
                stack.pop()
                if stack:
                    result.append(stack[-1])
    return result
```