```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> ['a', 3.14, 5] -> [5]
    >>> [1, 2, 3, 'abc', {}, []] -> [1, 2, 3]
    """
    return [int(x) for x in values if x.isinstance(int)]
```