Here is a Python script with a self-contained function that solves the problem of finding all prefixes from shortest to longest of a given string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Determine the length of the input string
    length = len(string)

    # Determine all prefixes from shortest to longest
    prefixes = [string[i:i+2] for i in range(length)] + [string]
    return prefixes
```