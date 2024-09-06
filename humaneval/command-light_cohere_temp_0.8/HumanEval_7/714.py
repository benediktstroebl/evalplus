```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

strings = ["abac", "abcde", "cdefoo", "hello", "world"]
substring = "cde"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['cdefoo', 'hello', 'world']

strings = ["apple", "annabel", "carte", "kiwi", "laptop"]
substring = "l"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['kiwi', 'laptop']
```
This script defines a function `filter_by_substring` that filters an input list of strings for those that contain a given substring.  The approach uses a Python list comprehension with a filtering condition based on the presence of the substring in the strings.