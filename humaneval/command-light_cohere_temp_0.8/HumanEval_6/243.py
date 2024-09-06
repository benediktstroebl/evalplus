```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for c in s:
        if in_string:
            if c == '(':
                stack.append(1)
                in_string = False
            continue
        elif c == ')':
            if len(stack) == 0:
                in_string = False
                continue
            top_level = stack.pop()
            if top_level == 0:
                in_string = False
                continue
            output.append(3)
        stack.
    return output
 return output
```