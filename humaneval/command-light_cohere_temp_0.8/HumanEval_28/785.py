Here is a self-contained Python script that defines a function `concatenate` that solves the problem of concatenating strings in a markdown code block:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([1,2,3])
    123
    """
    return "".join(strings)
```