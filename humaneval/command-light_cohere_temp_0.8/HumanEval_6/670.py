```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Remove spaces and split by parentheses
    s = s.replace(' ', '')
    tuple(map(int, (i for i in s if i == '('))))
    return [i for i, j in zip(flatten(t), '()') if j == ']' and i != ']']
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())')') == [2, 3, 1, 3]
```