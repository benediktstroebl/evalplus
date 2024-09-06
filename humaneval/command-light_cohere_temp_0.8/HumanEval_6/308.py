```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    for match in s:
        if match == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                res.append(3)
            stack.append(4)
        else:
            stack.append(None)
    else:
                stack.append(len)
    stack.append(match)
    return res
```