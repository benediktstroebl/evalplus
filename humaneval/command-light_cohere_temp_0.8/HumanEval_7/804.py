```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function called `filter_by_substring` that filters a list of strings for a given substring. It utilizes the `find()` function to search for the substring in each string, and returns the string if the substring is found.

The script also provides a set of test cases, which passes the `filter_by_substring` function to filter the list of strings for the given substring.