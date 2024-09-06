Here's the self-contained Python script with a function that solves the problem of concatenating strings in Markdown code blocks:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(s.join() for s in strings)
```