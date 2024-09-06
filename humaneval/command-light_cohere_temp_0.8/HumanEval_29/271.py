```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    >>> filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    >>> filter_by_prefix([ 'def', 'ghello', 'hi', 'World!  ', 'array'], 'ghello')
    []
    """
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that filters an input list of strings, retaining only those that start with a specified prefix. The function utilizes the `startswith` method from the string module to perform this filtering. The code is designed to handle any list of strings and any prefix, regardless of length. It can be a also used to filter strings based on a specific prefix, offering a flexible and reusable solution.