```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([':()]) # Empty string -> empty string
    >>> concatenate(['a', '', 'c']) # Trailing space -> 'a  c'
    >>> concatenate(['a', '  b']) # Extra space -> 'a  b'
    """
    return "".join(strings)
```