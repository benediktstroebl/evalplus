```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1: Empty input list
print(filter_by_substring([], 'a'))
# Output: []

# Test case 2: Single string
print(filter_by_substring(['a'], 'a'))
# Output: ['a']

# Test case 3: Multiple strings with substring
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
# Output: ['abc', 'bacd', 'array']

# Test case 4: Input list with substring not present
print(filter_by_substring(['def', 'ghi', 'jkl'], 'abc'))
# Output: []
```
This script defines a function `filter_by_substring` that filters a list of strings based on whether the given substring is present. It then passes four tests to verify its functionality. The tests are designed to validate the functionality of the function, passing all of them successfully.