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

# Test the function
values = [1, 2, 'three', 3, 'four', 5, 6]
print(filter_integers(values))  # [1, 2, 3, 5, 6]
```