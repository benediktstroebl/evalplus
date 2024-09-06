```python
from typing import List
def longest(strings: List[str]):
    """ Returns the longest string in the list.
    >>> longest(['a', 'b', 'ccc'])
    'ccc'
    >>> longest(['a', 'bb', 'cc'])
    'cc'
    >>> longest(['aa', 'bb'])
    Traceback (most recent call last):
      File "<string>", line 10, in <module>
    AssertionError: Lists must contain equal elements: ['aa', 'bb']
    """
    return max(strings, key=len)
```