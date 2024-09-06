Here is a Python script with a self-contained function that solves the problem of finding all prefixes from the shortest to longest of an input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(sorted(string, key=len))
```  This script provides a function that accepts a string as input and returns a list of its prefixes. The function uses the new style of Python, with type hints, to make the function self-contained and easier to understand.