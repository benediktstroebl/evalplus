Here is a Python script that contains a self-contained function that solves the problem of returning all prefixes from shortest to longest of an input string:
```python
from typing import List
import re


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return re.findall(r'\w+[^a-zA-Z]', string)
```