```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    for c in s:
        if c == '(': stack.push(len)
        elif c == ')': 
             while stack: stack.pop()
             if stack: stack.pop()
             return stack
    turn = True
    return []
```