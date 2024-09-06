Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List
import re

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if re.search(prefix, string)]
``` 
The function `filter_by_prefix` takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. It utilizes the pattern matching with the prefix to filter the strings in the list.