```python
from typing import List
def longest(strings: List[str]):
    """ Out of list of strings, return the longest one
    Return the first one in case of multiple strings of the same length.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=len)
```
 This code defines a function called longest that takes in a list of strings as input and returns the longest string in that list. It uses the max function along with the key argument set to len, which returns the length of the longest string.