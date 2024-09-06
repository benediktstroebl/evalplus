Certainly! Here is a Python script that contains a self-contained function `filter_by_prefix()` that solves the problem you described:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. 

The test cases demonstrate that the function works as expected.