Here's the corrected Python script:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join("".join(strings)
```
The corrected script uses the List[str] syntax to correctly pass a list of strings to the concatenate function. This ensures that the the string values are passed correctly and the function can perform its task without any issues.