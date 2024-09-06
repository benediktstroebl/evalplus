```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        elif c == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unexpected character")
            stack.pop()
       
    if c == '(': stack.append(0)
    elif c == ')': stack.append(len)
    if c == '(': stack.append(3)
    elif c == ')': stack.append(2)
    return stack
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of their depths of nesting. It uses a stack data structure to keep track of opening parentheses and their corresponding closing ones.