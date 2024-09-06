Here is a self-contained Python script that solves the problem and passes the tests:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    return ''.join(strings)
```
This script defines a function `concatenate` that takes in a list of strings and returns the concatenated string.