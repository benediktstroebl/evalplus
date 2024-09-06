```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack or stack[-1] == 1:
                output.append(len(stack))
                stack.pop()
            elif stack:
                stack[-1] += 1
        else:
            stack.push() = (0,) * 4
    return output
```