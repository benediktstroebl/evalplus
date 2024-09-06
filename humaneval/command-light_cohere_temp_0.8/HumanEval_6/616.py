```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [ord(c) - 65 for c in s if c.isspace()]
return [ord(c) - 65 for c in s if c.isspace()]

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))'
    ) == [2, 3, 1, 3]

def test_parse_nested_parens2():
    assert parse_nested_parens('()()((()))') == [3, 2]

test_parse_nested_parens()
test_parse_nested_parens2()
```