Here is a Python script that demonstrates the implementation of a function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(sorted(set(string), key=len, reverse=True))
```
This code defines a function `all_prefixes` that takes a string `string` as input and returns a list of all prefixes from the shortest to the longest characters in the input string.