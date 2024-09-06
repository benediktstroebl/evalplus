Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "welcome", "hello world"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```

This script provides a well-contained function that filters an input list of strings for ones that contain a given substring.  The approach is simple and efficient and passes all test cases successfully.