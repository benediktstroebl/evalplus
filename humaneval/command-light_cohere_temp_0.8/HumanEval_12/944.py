```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print(longest_result)  # Output: c

strings = ['aa', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: bb

strings = ['a']
strings. longest = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: a
```