```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_group = False
    for c in s:
        if c == '(':
            if not:
                in_group = True
                stack.append(1)
            else:
                stack.append(0)
        if c == ')':
            if len(stack) == 0:
                in_group = False
            else:
                stack.pop()
    if in_group:
                stack.append(1)
        return stack
```

This function parses a string of nested parentheses, returning a list of the deepest levels of nesting. It uses a 'stack' to keep track of the current parenthesis depth and appends to it the next level. The function also checks to ensure the stack is empty when a ')' is encountered to end a group and starts a new one.