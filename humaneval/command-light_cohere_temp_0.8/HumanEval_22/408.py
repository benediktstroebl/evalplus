```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers."""
    return [i for i in values if isinstance(i, int)]

# Test the function with various inputs
values_test = [1, 2, 3, 'abc', 3.14, 5]
print(filter_integers(values_test))  # Expected Output: [1, 2, 3, 5]

# Test with other data types
strings_test = ['abc', (1), 2.0]
print(filter_integers(strings_test))  # Expected Output: []

# Test with nested data
list_test = [['a', 3.14], [5]
print(filter_integers(list_test))  # Expected Output: [3.14, 5]
```