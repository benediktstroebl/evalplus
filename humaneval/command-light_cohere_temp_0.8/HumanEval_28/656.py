Here's the corrected self-contained Python function that performs the concatenation of strings in markdown code:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([''' multi \\"middle \\\"quotes'''])
    'multi \\"middle \\\"quotes'
    """
    return ''.join(strings)
```

This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the _ `return` statement to return the concatenated result.