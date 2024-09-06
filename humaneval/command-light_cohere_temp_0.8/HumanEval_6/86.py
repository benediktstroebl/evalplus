```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    result: List[int] = []
    for char in s:
        if char == '(':
            stack.append('(')
       
        elif char == ')':
            if stack:
                stack.pop()  #"""
            else:
                result.append(1)
                continue
        else:
            stack.append(char)
    continue
    return result
```