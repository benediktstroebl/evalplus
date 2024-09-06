```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Run the function with a test set
test_strings = ['abc', 'bcd', 'cde', 'array', 'xray', 'z'])
test_prefix = 'a'
result = filter_by_prefix(test_strings, test_prefix)
assert result == ['abc', 'array']
```