```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'begin']
prefix = 'array'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['array', 'cde']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It returns a The strings in the input list that start with the provided prefix, as specified by the `startswith` method.