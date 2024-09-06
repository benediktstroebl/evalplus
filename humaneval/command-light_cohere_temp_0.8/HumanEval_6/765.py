```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                stack.pop()
            stack.append(0)
   
    return stack
```