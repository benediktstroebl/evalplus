```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'b', 'cd'], 'a') == ['abc']
    assert filter_by_prefix(['list', 'list', 'aa', 'bc'], 'l') == ['list', 'list']
```