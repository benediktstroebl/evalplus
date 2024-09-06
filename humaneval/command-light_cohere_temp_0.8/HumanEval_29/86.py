Here is a self-contained Python script with a function that filters strings based on a given prefix:
```python
from typing import List
import re

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by a given prefix.

    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']

    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'be')
    []

    >>> filter_by_prefix(['abc', 'bebf', 'cde'], 'be')
    ['bf', 'cde']

    >>> filter_by_prefix(['abc', 'bebf', 'cde'], 'be')
    ['bf', 'cde']

    >>> filter_by_prefix(['abc', 'bcd', 'cdeda'], 'cd')
    ['cdeda']

    >>> filter_by_prefix(['abc', 'bcd', 'cdeda'], '')
    []

    """

    # Use a regular expression to filter strings
    pattern = re.compile(r'^[\w]+{prefix}\b')
    return [s for s in strings if pattern.search(s)]

```