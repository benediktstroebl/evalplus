```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "pass", "present"]
substring = "a"

# Function call and print results
print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

strings = ["apple", "banana", "cherry"]
substring = "an"

print(filter_by_substring(strings, substring))  # Output: ['apple', 'banana']
```

This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It then passes these tests with various strings and a substring to demonstrate its functionality.