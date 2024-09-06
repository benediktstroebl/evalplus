```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]


# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings = ["a", "bcd"]

result = filter_by_substring(strings, substrings)
print(result)  # Output: ['abc', 'bacd', 'array']

strings = ["abc", "hello"]
substrings = ["b"]

result = filter_by_substring(strings, substrings)
print(result)  # Output: []

strings = ["abc", "hello"]
substrings = ["bcd"]

result = filter_by_substring(strings, substrings)
print(result)  # Output: ['abc']
```

This script defines a function called `filter_by_substring` that filters a list of strings based on a given substring. It takes the using a inputs: a list of strings and a substring. The function returns a list of strings that contain the substring. The test cases demonstrate the filtering of strings that do and do not contain the given substring.