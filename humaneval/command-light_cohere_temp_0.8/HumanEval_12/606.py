```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['aa', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "<string>", line 7, in longest
      File "<string>", line 6:
      raise ValueError
    ValueError: Input list is empty
    """
    if not strings:
        raise ValueError("Input list is empty")

    return max(strings, key=len)
```