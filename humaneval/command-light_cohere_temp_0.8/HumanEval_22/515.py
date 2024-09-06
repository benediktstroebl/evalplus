```python
from typing import List
def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]
# Unit tests
values1 = [1, 2, 'three', (])
values2 = [True, 2, 3, 'four', [1, 2, 3])
values3 = [1, 2, 'three', None]

assert filter_integers(values1) == [1, 2]
assert filter_integers(values2) == [2, 3]
assert filter_integers(values3) == [1, 2]
```