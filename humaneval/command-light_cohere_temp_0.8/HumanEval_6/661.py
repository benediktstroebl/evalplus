```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    levels = []

    for char in s:
        if char == "(":
            stack.append([1])
            levels.append(1)
        while char == ")"
        elif char == ")":
            stack.pop()
            if char == "(":
                stack.append([0])
                levels.append(0)
            else:
                stack.append(char)

    return [max(levels)]
```