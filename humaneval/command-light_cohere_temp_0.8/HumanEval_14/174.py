Here is a Python script with a self-contained function that solves the problem of returning all prefixes from shortest to longest of an input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ["".join(c) for c in string]
```  This script defines a function all_prefixes that takes a string as input and returns a list of all prefixes in the input string, starting from the shortest to longest.