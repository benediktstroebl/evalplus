```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return []
            stack.append(0)
        else:
                return []
    return stack
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()')') == [2, 3, 1, 3]
```