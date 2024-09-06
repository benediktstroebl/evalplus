```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == "(":
            stack.append(1)
        elif c == ")":
            if len(stack) == 0:
                result.append(0)
            stack.remove_last()
       
        else:
            stack.append(0)
    stack.append(1)
    return result
```