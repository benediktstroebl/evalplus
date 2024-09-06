```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.add( ['abc', 'bcd', 'cde', 'array', 'a'], [
    'abc', 'array'
])
test_filter_by_prefix.add( ['a', 'b'], []
test_filter_by_prefix.add( ['a', 'ccc'], [])
test_filter_by_prefix.add( ['x', 'xx'], [])

def test_func(tst: List[str], pre: str) -> None:
    assert(filter_by_prefix(tst, pre) == test_filter_by_prefix)

test_func(test_filter_by_prefix, 'a')
```