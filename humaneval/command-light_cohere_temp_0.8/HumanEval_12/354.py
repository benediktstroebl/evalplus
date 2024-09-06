```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, returns the length of the longest one.
    >>> longest(['a', 'b', 'c'])
    ['a', 3]
    >>> longest(['aa', 'bb', 'ccc'])
    [3, 3]
    >>> longest([])
    Traceback (most recent call last):
      File "<string>", line 10:14: TypeError: cannot convert 'None' to int
    ValueError: list object is not iterable
    ```