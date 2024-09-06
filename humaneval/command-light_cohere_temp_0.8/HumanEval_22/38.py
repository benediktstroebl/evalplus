```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([1, 2, 'three', 123])
    []
    """
    result = [int(item) for item in values if item != '' and isinstance(item, int)]
    return result
```