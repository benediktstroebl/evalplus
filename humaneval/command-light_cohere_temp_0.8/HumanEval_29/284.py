Here is a Python script with a self-contained function that solves the problem of filtering strings starting with a prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([('ab'*10), 'a'), 'a')
    ['('ab'*10), 'a']
    """
    return [x for x in strings if x.startswith(prefix)]
```
This script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix as input, and returns a new list of strings that start with that prefix.