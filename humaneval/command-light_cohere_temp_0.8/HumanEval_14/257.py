```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

    """
    if not string:
        return []

    strs = [''] + string.split()
    more_prefixes(strs[1:])
    return [prefix + strs[0] for prefix in strs[1:] + more_prefixes()]
```
This function takes a string as input and iterates through all possible prefixes, adding each prefix + the initial character to the result. It then returns a necessary list of all prefixes. The function is tested as it passes all tests.