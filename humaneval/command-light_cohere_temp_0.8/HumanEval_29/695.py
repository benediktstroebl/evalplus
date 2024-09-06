```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test case: Filter strings that start with 'a'
test_case = ['abc', 'bcd', 'cde', 'array', 'for', 'hello']
assert filter_by_prefix(test_case, 'a') == ['abc', 'array'],
```