```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    out = []
    for char in parenthes_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                stack.append(0)
            elif stack[-1] == int(char):
                stack.pop()
            out.extend([stack.append(stack[-1])])
    else:
                stack.append(stack[-1])
    out.append(char)
    return out
```