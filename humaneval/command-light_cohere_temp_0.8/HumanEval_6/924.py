```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_levels = 0
    closing_levels = 0

    for char in parentheses_string:
        if char == "(":
            if opening_levels == 0:
                opening_levels += 1
            stack.append(opening_levels)
        elif char == ")":
            closing_levels = stack.pop()
            if closing_levels == 0:
                closing_levels -= 1
                if closing_levels == 3:  # Matching top level of three closing parentheses
                    return [closing_levels]
    return []
```