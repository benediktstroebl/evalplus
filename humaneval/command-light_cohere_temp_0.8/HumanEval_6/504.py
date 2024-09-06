```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    start_level = 0
    output = []
    for c in s:
        if c == '(':
            stack.append(start_level)
            start_level += 1
        elif c == ')':
            stack.pop()
           while stack and not empty:
                output.append(stack.pop()
               max()
                stack.append(start_level)
            start_level = 0
    return output
def test_parse_nested_parens() -> None:
    input = "(()()) ((())) () ((()))"
    assert parse_nested_parens(input) == [2, 3, 1, 3]
    return None
```