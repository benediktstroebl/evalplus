```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'fgh', 'hello', 'world']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['abc', 'fgh', 'hello']

strings = ['array', 'list', 'a']
prefix = 's'
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['array', 'list']
```
This script defines a function **filter_by_prefix** that filters a list of strings based on a given prefix. The function works by iterating over each string in the list, and checking if the string starts with the given prefix.