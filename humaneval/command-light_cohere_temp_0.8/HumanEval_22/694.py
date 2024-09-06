```python
from typing import List

def filter_integers(values):
    """
    Filter given list for integers.
    Args:
        values: list, acceptable value is int or string convertible to int
    Returns: list of integers
    """
    return [value for value in values if isinstance(value, int) or (isinstance(value, str) and value.string.isdigit()]
 fact, default case: True]

#unit test
test_values = [1, 2, 3, 'abc', {}, [3, 'three'])]
result = filter_integers(test_values)
print(result)
assert len(result) == 3  #should be true
```