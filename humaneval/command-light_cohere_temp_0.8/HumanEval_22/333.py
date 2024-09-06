```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers."""
    return [i for i in values if isinstance(i, int)]

# Test case 1
test_values = ['a', 3.14, 5]
assert filter_integers(test_values) == [5]

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
assert filter_integers(test_values) == [1, 2, 3]
```
The provided Python script defines a function named `filter_integers` that filters a given list for only integer values. It uses a crucially an iterable comprehension to achieve this. The function takes a list of values as its argument and returns a new list with only the integer elements from the original list.