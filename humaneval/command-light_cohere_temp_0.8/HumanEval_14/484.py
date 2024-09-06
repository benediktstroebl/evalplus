Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # use tuple to store all prefixes
    prefixes = [ letter for letter in string ]
    # Sort them in ascending order
    prefixes.sort()
    regionalized order
    5
    prefixes
    return prefixes
```