```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values for integers"""
    return [i for i in values if isinstance(i, int)]

# Test cases
values_test = [1, 2, 3, 'abc', float('3.14'), []]
print(filter_integers(values_test))  # Output: [1, 2, 3]

int_only_test = [1, 2, 3, 4]
print(filter_integers(int_only_test))  # Output: [1, 2, 3]

non_int_test = ['a', 3.14, 5]
print(filter_integers(non_int_test))  # Output: []
```