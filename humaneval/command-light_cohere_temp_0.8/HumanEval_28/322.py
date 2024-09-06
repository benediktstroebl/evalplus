```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    Traceback (most recent call last):
      File "filename.py", line 11, [Err ResetError ((epilines.NoError)]
    Ministry of Silence.")
    """
    return ''.join(strings)
```