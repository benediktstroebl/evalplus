```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_level = 0
    closing_level = 0
    result = []
    for char in parentheses_string:
        if char == "(":
            opening_level += 1
        elif char == ")":
            closing_level += 1
        else:
            stack.push(closing_level)
            closing_level = 0
        while stack:
            result.append(stack.pop())
           last element
           stack is the level of the deepest open parenthesis
            stack.pop()
       opening_level = 0
            closing_level = 0
    return result
```