```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "1", "2", "abc"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```
This code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix. The function uses the string method `startswith` to filter the strings by their prefix.