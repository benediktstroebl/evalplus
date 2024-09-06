```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    in_string = False
    nesting_level = 0
    result = []
    for char in parenthes:
        if char == " ":
            if not in stack:
                stack.append(nesting_level)
            nesting_level = 0
        elif char == "(":
            if not in stack:
                stack.append(nesting_level + 1)
                in_string = True
            else:
                stack.append(nesting_level)
        elif char == ")":
            if in_string:
                result.append(stack.pop()
                deepest_level)
                stack.remove()
                in stack
                in_string = False
        else:
            stack.append(nesting_level)
    return result
```