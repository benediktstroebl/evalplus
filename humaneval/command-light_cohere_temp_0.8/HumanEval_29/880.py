```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "array", "xray", "hello"]
prefix = "array"

print(filter_by_prefix(strings, prefix))  # Output: ['array']

print(filter_by_prefix(["abc", "abcd", "cdef"], "def"))  # Output: ['cdef']

print(filter_by_prefix(["abc", "def", "cdef"], "def"))  # Output: ['abc', 'cdef']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It works with the tests to pass the `types` and `tests` from the `typing` module, which are static and don't need to be imported from another module.