```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Expected output: ['abc', 'bacd', 'array']
result = filter_by_substring(strings, substring)
print(result)

strings = ["abc", "cde", "hello", "world"]
substring = "dl"

# Expected output: []
result = filter_by_substring(strings, substring)
print(result)
```

This code defines a function `filter_by_substring` that filters a list of strings for a given substring. It then passes these tests to demonstrate the functionality.