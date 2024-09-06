```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case: Filter words that start with 'a'
test_case = [
    'abc', 'bcd', 'cde', 'array', 'anime', 'abox'
]
result = filter_by_prefix(test_case, 'a')
assert result == ['abc', 'array'], "The result is incorrect."
```