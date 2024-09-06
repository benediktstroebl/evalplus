```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Tests
test_filter_by_prefix = []
test_filter_by_prefix.add("'. ['abc', 'bcd', 'cde', 'array', 'ab'])
test_filter_by_prefix.add('''a''')
test_filter_by_prefix.add('zba.')
test_filter_by_prefix.add(None)
test_filter_by_prefix

def test_func(test_case):
    test_filter_by_prefix = test_case.filter_by_prefix(test_case, 'x')
    assert filter_by_prefix == test_case

# Test cases
test_filter_by_prefix
```