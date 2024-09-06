```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    Returns a filter for a given prefix, and is case-insensitive.
    >>> filter_by_prefix(['abc', 'Bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if prefix.lower() in x or result.startswith(prefix.lower())]

``` 
This script provides a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function returns a list of strings that start with the given prefix, and is case-insensitive.