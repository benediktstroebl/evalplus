```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.append([
    'abc', 'a'])
test_filter_by_prefix.append(['cde', 'bcd'])
test_filter_by_prefix.append(['cde', 'array'])
test_filter_by_prefix.append('bc')
assert filter_by_prefix(test_filter_by_prefix, 'a') == ['abc'])
assert filter_by_prefix(test_filter_by_prefix, 'bcd') == ['cde', 'bc']
```