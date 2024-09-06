```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
test_strings = ['abc', 'bcd', 'cde', 'a', 'array', 'begin', 'for']
test_prefix = 'a'

result = filter_by_prefix(test_strings, test_prefix)
assert len(result) == 3  # should be 'abc', 'array'

# Normal usage
result = filter_by_prefix([40, 41,42,' ZOO','.join')
assert result == ['40','. Hanson', '42'])
```