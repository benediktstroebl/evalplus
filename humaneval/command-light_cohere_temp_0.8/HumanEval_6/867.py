```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for c in s:
        if c == '(':
            if not:
                in_string = True
            stack.append(1)
        if c == ')':
            if len(stack) == 0:
                in_string = False
            else:
                stack.pop()
        if in_string:
                stack.append(3)
                output.append(stack.pop())
    all items on stack are now 3, 2, 1, 3, 3, 2, 1, 3. this order
return output
```