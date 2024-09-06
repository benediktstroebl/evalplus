```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'cde'
result = filter_by_prefix(strings, prefix)
print(result)

strings = ['abc', 'bcd', 'cde', 'hello', 'world']
prefix = 'x'
result = filter_by_prefix(strings, prefix)
print(result)
```
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains elements starting with the specified prefix.  The tests that generate test cases for the function, which successfully filter the strings.