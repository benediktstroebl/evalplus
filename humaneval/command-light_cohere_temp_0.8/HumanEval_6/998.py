```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_level = 0
    result = []
    for c in s:
        if c == '(':
            open_level += 1
        elif c == ')':
            open_level -= 1
        else:
            stack.push(open_level)
        result.push(stack.pop())
    plain parentheses.
    return result

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()') == [2, 3, 1, 3]
```