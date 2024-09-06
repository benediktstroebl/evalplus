```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.append(['abc', 'bcd', 'cde', 'array', 'adfa'])
test_filter_by_prefix.append('hello')
assert filter_by_prefix(test_filter_by_prefix, 'a') == ['abc', 'array'],

test_filter_by_prefix.assert assert filter_by_prefix(test_filter_by_prefix, 'x') == [],

test_filter_by_prefix. assert assert filter_by_prefix(test_filter_by_prefix, 'cd') == ['cde'],
```