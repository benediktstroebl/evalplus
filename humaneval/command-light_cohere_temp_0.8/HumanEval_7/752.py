Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings for the given substring
    >>> filter_by_substring([])     []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'bd')
    []
    """
    return [string for string in strings if substring in string]
```

This script defines a function `filter_by_substring` that filters an input list of strings for a given substring. It takes a an example of how to use this function to filter a list of strings for a specific substring. The test cases demonstrate that the function works correctly.