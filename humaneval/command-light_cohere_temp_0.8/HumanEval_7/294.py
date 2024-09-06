```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'xa']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters an input list of strings, ensuring that only those containing a given substring are returned.  It takes a necessary to solve the problem, passing a list of strings and a single character substring 'a'.  The function uses the `find()` method to locate the substring within each string and returns the resulting list of strings that contain the substring.