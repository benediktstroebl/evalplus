```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([0, 1, 2, 'three', 3.0])
    [2, 3]
    >>> filter_integers([0, 2, 'three', 3.0])
    [2, 3]
    """
    return [x for x in values if type(x) == int]
```