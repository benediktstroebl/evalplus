```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Testing the function
test_strings = [
    "abc", "bcd", "cde", "array", "hello", "world", "compound"
]

test_prefix = "a"

result = filter_by_prefix(test_strings, test_prefix)
print(result)  # Output: ['abc', 'array']
```
This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix, then returns a new list that contains only the strings from the input list that start with the provided prefix. The code also includes a test suite that passes the function with a test prefix and prints the resulting filtered list.