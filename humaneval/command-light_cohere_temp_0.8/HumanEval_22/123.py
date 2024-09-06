```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [num for num in values if isinstance(num, int)]

#Test cases
values1 = [1, 2, 3, 'abc', ]
values2 = [1, 2, 3, 'a', 4]
values3 = [1, 2, 3, 'b', 5]

print(filter_integers(values1))  # [1, 2, 3]
print(filter_integers(values2))  # [1, 2, 3]
print(filter_integers(values3))  # []
```