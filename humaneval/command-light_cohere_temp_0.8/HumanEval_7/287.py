```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


# Example usage:
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a list comprehension to iterate over the input strings and returns only the strings that contain the given substring.