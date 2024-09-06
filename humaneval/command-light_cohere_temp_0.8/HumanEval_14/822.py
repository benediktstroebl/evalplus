Here is a Python script that contains a self-contained function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string"""
    return list(itertools.chain(sorted(''.join(string)))
```
This script provides a function that takes a string as input and returns a list of all its prefixes.  The approach uses the using the 'itertools.chain' function which takes the sort of characters in the string from shortest to longest. The function then returns the list of these sorted characters.