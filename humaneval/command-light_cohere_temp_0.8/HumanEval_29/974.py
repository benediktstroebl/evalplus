```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Run unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_str('')
test_filter_by_prefix.push_str('a')
test_filter_by_prefix.push_str('ab')
test_filter_by_prefix.push_str('abc')
test_filter_by_prefix.push_str('bcd')
test_filter_by_prefix.push_str('cde')
test_filter_by_prefix.push_str('array')
test_filter_by_prefix.push_str('!sted')
def test_filter_by_prefix() -> None:
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd', 'cde']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'cde') == ['cde']
    assert filter_by_prefix(['abc', 'def', 'gair', 'array'], 'air') == []
```