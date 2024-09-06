```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list of strings.
    >>> longest([])
    >> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'a'])
    Traceback (most recent call last):
      File "<filename>", line 6, in <module>
        raise ValueError("Input list is empty")
    ValueError: Input list is empty
    """
    if not strings:
        raise ValueError("Input list is empty")
    return max(strings, key=len)
```