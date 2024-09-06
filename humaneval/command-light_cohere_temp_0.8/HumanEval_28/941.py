Certainly, here's a self-contained Python script that defines a function `concatenate` solving the problem of joining a list of strings into a single string, and passing the tests:

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcd'
    """
    return "".join(strings)
```