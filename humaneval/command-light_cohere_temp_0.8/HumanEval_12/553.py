```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list, or None if empty.
    """ 
    if not strings:
        return None

    longest_length = max(len(str) for str in strings)
    longest_char = strings[0][:longest_length]
    return longest_char

# Unit tests
strings = ["abcd", "abcba", "abcd", "abc"]
assert longest(strings) == "abcd"
strings = ["a", "bb", "abc"]
assert longest(strings) == "ab"
```