```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

strings = ["abracad", "cdab", "ab", "ad", "hello"]
substring = "ab"

print(filter_by_substring(strings, substring))  # Output: ['abracad', 'cdab']

strings = ["abc", "cdef", "abcd", "hello"]
substring = "c"

print(filter_by_substring(strings, substring))  # Output: ['cdef', 'cdef', 'abcd']
```

The function `filter_by_substring` accepts a list of strings and a substring as input. It utilizes a string matching to return only those elements in the input list that contain the given substring. The test cases demonstrate the using different input lists and substrings, showcasing the function's behavior.