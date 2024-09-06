```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(accumulate(string, str. all.split()))
```
```
This code defines a Python function all_prefixes that accepts a string as input and returns a list of all prefixes from shortest to longest. The function uses the string. The type hint is added to the function to provide better code documentation and type-checking.