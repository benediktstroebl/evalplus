```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(': stack.append(1)
        else:
            if not stack or c == ')':
                result.append(len)
                stack.append(None)
            else:
                stack.append(c)
    return result
```