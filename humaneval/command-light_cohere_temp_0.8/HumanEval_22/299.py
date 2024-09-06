```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([10, 20, 'hello', 35, 2.05])
    [10, 20, 35]
    """
    return [x for x in values if type(x) == int]
```