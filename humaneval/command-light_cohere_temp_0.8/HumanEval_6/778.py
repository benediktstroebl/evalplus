```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, ch in enumerate(s, 2) if ch == '(']

# Tests
assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
assert parse_nested_parens('((()()))') == [1, 2]
assert parse_nested_parens(')()()()()()()()()()()()()()()()') == []
assert parse_nested_parens('(,))') == []
assert parse_nested_parens(')()' == []
assert parse_nested_parens('()(') == [1]
```