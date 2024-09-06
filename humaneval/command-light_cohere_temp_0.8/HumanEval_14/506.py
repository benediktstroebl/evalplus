```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    # use the alphabet size to get all prefixes
    alphas_size = len('abcdefghijklmnopqrvwxyz')
    prefixes = []
    for i in range(1, al_size + 1):
        prefixes.append( chr(96 + i - 96 - 65 + int(string[0] == str[0])) )
    return prefixes
```