```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            stack.append(char)
   
    while stack:
        else:
            for _ in stack:
                result.append(_ + 1)
            stack = []
    return result
```