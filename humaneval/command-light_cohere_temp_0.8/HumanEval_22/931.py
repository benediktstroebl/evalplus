Here's a self-contained Python script that defines a function **filter_integers**, which takes a list of any python values as input and returns a list of integers:
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
# Unit tests
test_values = [1, 2, 3, 'abc', [1, 2, 3], {}]
test_output = filter_integers(test_values)
assert test_output == [1, 2, 3]
```