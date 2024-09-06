```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    open_level = 0
    for char in s:
        if char == '(':
            open_level += 1
        elif char == ')':
            open_level -= 1
        else:
            stack.append(open_level)
        result.append(stack.pop())
   .
    return result

    assert len(result) == 3, "Expected 3 items in the output list"
    assert open_level == 0, "Expected all parentheses to be closed"
    assert len(stack) == 0, "Expected no open parentheses left"
    return result
```