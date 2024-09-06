```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    result: List[int] = []
    for ch in s:
        if ch == '(':
            stack.append(')')
       
        elif ch == ')':
            stack.pop()
        with stack:
                result.append(stack.pop().this.
    return result
return result
```