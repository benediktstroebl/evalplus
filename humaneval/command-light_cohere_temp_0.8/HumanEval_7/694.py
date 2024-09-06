```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [str for str in strings if substring in str]

# Test cases
strings = ["abc", "hello world", "hello how are you"]
substring = "ow"
expected = ["hello world", "hello how are you"]

print(filter_by_substring(strings, substring))
print("Expected:", expected)
```