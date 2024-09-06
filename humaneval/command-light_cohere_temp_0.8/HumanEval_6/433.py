```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []

    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                stack.append(0)
            elif stack[-1] == '(':
                stack.append(2)
                else:
                stack.append(3)
                output.append(stack.pop())
   array()
   array()

    return output
```