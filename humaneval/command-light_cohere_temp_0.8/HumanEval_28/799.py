Here is a Python script that includes the function `concatenate`, which accepts a list of strings and returns a concatenated string:

```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```

This script provides a test case that passes and includes an example that demonstrates the usage of the `concatenate` function.