Here is a self-contained Python script that includes the function `filter_by_prefix` which solves the problem you described: 
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([], 'a') == []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['abc', 'cdef'], 'b'))  # Output: []
``` 
This script provides a function to filter a list of strings based on their prefix, and includes several test cases to demonstrate its functionality.