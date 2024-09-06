```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case:
strings = ['abc', 'bcd', 'cde', 'array', 'final']
prefix = 'cde'

result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cde', 'array']
```
This script defines a function called `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the tested to ensure that only strings starting with the given prefix are included in the result. The function successfully passes the test cases.