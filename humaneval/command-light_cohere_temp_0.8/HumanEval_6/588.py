```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    stack.append(0)
    for i, char in enumerate(s):
        if char == '(': stack.append(1)
        elif char == ')': stack.append(0)
        if char == '(' and stack[-1] == 1: stack.pop()
        for i, char in enumerate(s):
            if char == ')': stack.append(1)
            elif char == '(' and stack[-1] == 0: stack.append(0)
            elif char == ')' and stack[-1] == 1: stack.pop()
            if len(stack) > 0: return stack
```