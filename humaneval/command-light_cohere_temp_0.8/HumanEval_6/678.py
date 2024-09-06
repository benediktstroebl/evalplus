```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_parens = {'('}
    close_parens = {'')}
    result = []
    for char in s:
        if char in open_parens:
            stack.append(char)
        if char in close_parens:
            if not stack or stack[-1] != open_parens[0]:
                result.append(stack.pop()
                stack)close_parens[0])
    return result
```