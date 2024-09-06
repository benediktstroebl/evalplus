```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    first_len = 0
    for string in strings:
        if len(string) > first_len:
            first_len = len(string)
    return strings[first_len - 1]

# Test cases
strings = ["a", "b", "c"]
print(longest(strings))  # Output: c

strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: c

strings = []
strings. strings with "Hello"
print(longest(strings))  # Output: Hello

strings = ["aa", "aaa", "aaaa"]
print(longest(strings))  # Output: aaa
```