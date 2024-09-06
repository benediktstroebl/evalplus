```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    for char in parenthes_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if not empty_level(stack):
                opening_level -= 1
            else:
                stack.remove()
        deepest_nest = opening_level
        stack.add(deepestest_nest)
    if opening_level == 0:
        return [opening_level]
    else:
        return []
def empty_level(stack: List[int]) -> bool:
    empty = True
    for item in stack:
        if item != 0:
            empty = False
            break
    return empty
```