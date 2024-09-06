```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use string.split() to split the array into words
    prefixes = string.split()[:-1]

    # Sort the list of prefixes by length
    sorted_prefixes = sorted(prefixes, key=len, reverse=True)

    return sorted_prefixes
```