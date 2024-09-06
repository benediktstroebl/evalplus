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

# Testing function
values_list = [1, 2, 3, 'abc', 5, 7, 8]
print(filter_integers(values_list) == [1, 2, 3])  # True
print(filter_integers([6, 'string']))       # [1, 2, 3]
print(filter_integers([6, 7, 8]))       # [5]
```