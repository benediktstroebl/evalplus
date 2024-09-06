```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'a1', 'array', 'bracket']
prefix = 'a'

# Expected Output
print(filter_by_prefix(strings, prefix))  # ['abc', 'a1', 'array']
```