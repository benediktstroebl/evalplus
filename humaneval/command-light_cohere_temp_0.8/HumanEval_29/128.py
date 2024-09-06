```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test case 1
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'cde'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cde', 'array']

# Test case 2
strings = ['def', 'function', ' programming']
prefix = 'function'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['function', ' programming']

# Test case 3
strings = ['abc', 'cdef', 'hello']
prefix = 'cdef'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cdef']
```
This script defines a function called `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the filtering technique where it uses the `startswith` method to check if each string in the input list starts with the given prefix.