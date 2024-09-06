Here's a self-contained Python script that implements the function `filter_by_prefix` as described:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')       []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```
This script provides a function `filter_by_prefix` that accepts a list of strings and a prefix. It uses the list comprehension to filter the strings in the list that start with the given prefix. The function is designed to pass all the tests mentioned in the problem statement.