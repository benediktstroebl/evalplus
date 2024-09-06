```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 1
    output = []

    for char in s:
        if char == " ":
            opening_level += 1
        elif char == ")":
            if stack:
                output.push(stack.pop(opening_level))
            opening_level -= 1
            stack.pop()
       else:
            stack.push(opening_level)

    return output
```