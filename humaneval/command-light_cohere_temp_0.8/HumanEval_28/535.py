Here is a Python script that solves the problem of string concatenation in Markdown code blocks: 

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
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcdef'
    """
    return ''.join(strings)
```