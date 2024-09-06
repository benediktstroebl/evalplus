```python
# The following code is copied verbatim from the original response
# The typeshed package needs to be installed to eliminate the warning

from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```