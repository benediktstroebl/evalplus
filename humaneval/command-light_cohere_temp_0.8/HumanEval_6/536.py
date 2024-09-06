```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    levels: List[int] = []

    for char in s:
        if char == "(":
            stack.append(len)
        elif char == ")":
            if not stack or stack[-1] == 0:
                stack.pop()
               else:
                stack.append(levels.append(stack.pop())
               while stack.append(0))
                levels.append(1)
        stack.append(char)

    # print(levels)
    return levels
```