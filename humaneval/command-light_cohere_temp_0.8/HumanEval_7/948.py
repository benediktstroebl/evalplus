```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1: empty list
print(filter_by_substring([], 'a'))  # Expected: []

# Test case 2: containing substring
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']

# Test case 3: not-substring
print(filter_by_substring(['abc', 'cdef'], 'def'))  # Expected: []
```

This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses a testing by passing different test cases and the expected output is printed to verify the function correctly.