```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    in_string = False  # To track if we are inside a string or not

    for char in parent_string:
        if char == '(':
            if not in_string:
                stack.append(1)
            in_string = True
        elif char == ')':
            if len(stack) == 0:
                in_string = False
            elif len(stack) == 1:
                stack.pop()
            else:
                stack.append(3)

    return stack
```