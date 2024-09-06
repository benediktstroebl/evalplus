```python
from typing import List
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    >>> values = ['a', 3.14, 5]
    [int]
    >>> values = [1, 2, 3, 'abc', {}, []]
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Test the function with sample inputs
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert isinstance(result, list), "Filtering failed"
assert len(result) == 3, "Filtering returned the wrong length"

# Print the filtered values
print("Filtered Values:", result)
```