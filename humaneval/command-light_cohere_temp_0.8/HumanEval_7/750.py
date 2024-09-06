```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring(['abc', 'bac', 'cde'], 'b')
    []
    """
    return [x for x in strings if substring in x]

# Tests
strings = ["abc", "hello", "world"]
sub = "hello"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['hello']
```