```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> strings = ['a', 'b', 'c']
    return longest(strings) # ['a', 'b', 'c']
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'bb'])
    Traceback (most recent call last):
      File "<stdin>", line 7, line 1:
        TypeError: 'str' object does not support item assignment
    >>> longest(['a', 'ab'])
    Traceback (most recent call last):
      File "<stdin>", line 7, line 7:
        'a' not found
    """
    if not strings:
        return None
    return max(strings, key=len)  # using built-in max function with key=len
```