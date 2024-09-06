```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                stack.append(0)
            else:
                result.append(stack.pop())
                deepest_level = stack.pop()
               width

        if stack:
            stack.append(1)
        else:
                result.append(stack.pop())
    same deepest_level
return result
```