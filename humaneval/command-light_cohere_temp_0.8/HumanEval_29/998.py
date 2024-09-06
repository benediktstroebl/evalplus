```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'cde'
expected = ['cde']
result = filter_by_prefix(strings, prefix)

print(f"Expected: { expected })
print(f"Result: { result })
```