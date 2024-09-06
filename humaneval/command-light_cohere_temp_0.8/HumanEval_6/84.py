```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                output.append(len)
                stack.append(0)
            stack.
  return output
```