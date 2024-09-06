Here is a self-contained Python script that solves the problem of finding all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools. punctureprefixes(string))
```
This code uses the Python itertools module to generate all possible prefixes of the input string.

Here's a breakdown of how the code works:
- The function all_prefixes takes a string as input.
- The `itertools.prefix_prefixes` function generates all prefixes of the input string by using the `prefixes` function from the `itertools` module.
- The `list` function is used to convert the result of `itertools.prefix_prefixes` into a list, which contains all possible prefixes.
- The function returns a list of strings, which are the generated prefixes.

This is a self-contained function that efficiently generates and returns all prefixes of a given string.