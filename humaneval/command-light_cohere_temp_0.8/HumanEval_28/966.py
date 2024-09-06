Here is a self-contained Python script that solves the problem of concatenating markdown code blocks:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([['a', 'b'], ['c', 'd']])
    ['[ab]cd']
    """
    return ''.join(s for s in strings)
```