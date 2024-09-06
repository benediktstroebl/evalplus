```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


# Test suite
strings = ["abc", "b Acd", "c De", "aarray"]
substrings = ["a", "bc", "c"]

# Function call and print results
print(filter_by_substring(strings, substrings))  # Expected output: ['abc', 'b Acd', 'c De', 'aarray']
```
This code defines a function **filter_by_substring** that filters a list of strings for a given substring using the in-built Python list method **contains**. The function takes a list of strings and a substring as input and returns a new list that contains only the strings that contain the given substring.