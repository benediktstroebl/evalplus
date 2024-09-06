```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate(['aa', 'b'])
    Traceback (most recent call last):
      File "<string>", line 8, in <module>
        concatenate(...): ValueError: invalid literal for int()
  """
    return ''.join(strings)
```