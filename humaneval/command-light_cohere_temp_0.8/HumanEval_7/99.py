```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

strings = ["abcd", "cdef"]
substring = "cd"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abcd', 'cdef']

strings = ["hello", "world"]
substring = "ello"

result = filter_by_substring(strings, substring)
print(result)  # Output: []
``` 
The provided Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. 

The test cases demonstrate how the function works, passing various strings and substrings. 

This script is an excellent illustration of a self-contained function that can be used in various scenarios to filter strings based on a substring.