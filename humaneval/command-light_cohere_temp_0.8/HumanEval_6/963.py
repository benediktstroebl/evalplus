```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [level for level in range(3, max(map(len, s)) for s in s. ]
def test_parse_nested_parens() -> None:
    # Test 1
    assert parse_nested_parens('(()()) ((())) () ((()))')') == [2, 3, 1, 3]
    # Test 2
    assert parse_nested_parens('() (()()())') == [0, 1]
    # Test 3
    assert parse_nested_parens('() ()()()()()()()()') == []
    return None
```