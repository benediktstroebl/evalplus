```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This code snippet demonstrates a Python function named **filter_by_prefix** that filters a list of strings based on a given prefix. The function utilizes the Python's **startswith** method to check if each string in the list starts with the specified prefix.