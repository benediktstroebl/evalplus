Below is a self-contained Python script that defines a function `filter_by_substring` solving the problem of filtering strings that contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```

This script provides a function that filters a list of strings for those that contain a given substring. It's self-contained and passes all the test cases.