Here is a self-contained Python script that solves the problem of finding all prefixes from the shortest to the longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(sorted(string, key=len, reverse=True))
```
This script defines a function all_prefixes that takes a string as input and returns a list of its prefixes. 
The sorted() function with the key=len sorts the string's characters by their length, and the reverse=True parameter ensures that the shortest characters come first. The sorted result is then converted back to a list of strings.