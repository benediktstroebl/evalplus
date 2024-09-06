```python
from typing import List
def longest(strings: List[str]):
    """
    Out of list of strings, returns the longest one.
    >>> longest([]) and []
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a'])
    Traceback (most recent call last):
      File "< SharpReader.py>", line 10, CharacterErrorError: 'must begin with an expression or assign to a variable'
    """
    # check if empty
    if not strings:
        return None
    # try-catch block to handle different cases
    try:
        return max(strings, key=len)
    except ValueError:
        return None
```