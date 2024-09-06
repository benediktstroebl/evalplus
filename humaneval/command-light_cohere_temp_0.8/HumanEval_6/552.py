```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    n = 0
    for c in s:
        if c == "(": n += 1
        stack.append(n)
        if c == ")": n -= 1
        if n == 0: break
    return stack


# Test cases go here
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((()))") == [2, 3, 1, 3]
    assert parse_nested_parens("((((())))()  ))()") == [2, 3]
    assert parse_nested_parens("(()))()()  ))()") == []
```