```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Testing the function with various inputs
test_strings = ['abc', 'bcd', 'cde', 'a', 'array', '!'*1']
test_prefix = 'a'

result = filter_by_prefix(test_strings, test_prefix)
assert result == ['abc', 'array'], "Function didn't return expected output"
```