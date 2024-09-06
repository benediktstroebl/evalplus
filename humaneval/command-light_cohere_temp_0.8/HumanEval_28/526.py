```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([
        "Hello, World!", 
        "Hello, Universe!",
        "Hello, Moon!"
    ])
    'Hello, World!'
    """
    return ''.join(strings)
```