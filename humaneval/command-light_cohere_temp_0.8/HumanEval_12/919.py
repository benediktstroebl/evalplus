```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    >>> longest([])
    >>> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['aa', 'b'])
    Traceback (most recent call last):
      File "<stdin>", line 75: ValueError: unexpected token '>' in input string
    ```