```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for char in parentheses_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                result.append(len())
                stack.append(0)
            else:
                stack.append(stack.pop()
   
        - open(0)
                stack.append(0)
            stack.append(1)
        stack.append(0)
        stack.append(1)
    stack.append(0)
    stack.append(0)
    stack.append(1)

    return result
```