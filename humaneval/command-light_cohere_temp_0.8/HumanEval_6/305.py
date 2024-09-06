```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    output = []
    for c in parenthes_string:
        if c == '(':
            stack.append(1)
        else:
            if not stack or c == ')':
                stack.append(0)
            else:
                stack.append(stack.pop(-1)
                level = 1
                output.append(level)
    return output
```
Do you require any other assistance with your task?