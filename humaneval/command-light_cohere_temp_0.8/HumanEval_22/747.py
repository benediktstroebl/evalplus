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

# Testing the function with a variety of inputs
values_list = [
    None, 
    'abc', 
    1, 
    2, 
    3, 
    4, 
    5, 
    6, 
    7, 
    8, 
    9, 
    10, 
    [1, 2, 3], 
    []
]

print(filter_integers(values_list))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```