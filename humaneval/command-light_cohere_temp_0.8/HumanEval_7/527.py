```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]


# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
``` 
This code defines a function `filter_by_substring` that filters an input list of strings based on a given substring. The function uses the search to determine if each string contains the given substring.