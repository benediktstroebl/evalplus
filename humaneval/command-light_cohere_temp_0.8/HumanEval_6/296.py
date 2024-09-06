```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == "(":
            stack.append(0)
        elif char == ")":
            stack.pop()
            if len(stack) == 0:
                result.append(1)
        else:
                result.append(stack.pop() + 2
        result)
    return result
```