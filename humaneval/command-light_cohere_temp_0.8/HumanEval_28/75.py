```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([])["foo"]
    "foofoo"
    >>> a = ['a', 'b', 'ccc']
    >>> concatenate(a)
    'abcccc'
    """
    return "".join(strings)
```