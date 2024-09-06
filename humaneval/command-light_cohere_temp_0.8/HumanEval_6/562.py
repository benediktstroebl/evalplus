```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = False
    closing = False
    in_group = False
    for char in s:
        if char == '(':
            if opening:
                stack.append(1)
            opening = False
            in_group = True
        elif char == ')':
            if not_closing:
                stack.append(3)
            closing = False
            in_group = False
        elif char == '(':
            closing = True
        elif char == ')':
            if in_group:
                stack.append(1)
            in_group = False
        else:
            continue
        if in_group:
            stack.append(char)
    if stack:
            return stack
    else:
        return []
# tests
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
assert parse_nested_parens(')()) ((())) () ((())()())' == [2, 3, 1]
assert parse_nested_parens('(((((())))))))()') == [4]
assert parse_nested_parens('(((()))))())()()()()()()()' == [1, 2]
```