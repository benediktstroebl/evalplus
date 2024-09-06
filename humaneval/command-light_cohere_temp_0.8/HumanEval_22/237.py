```python
from typing import List
def filter_integers(values):
    """Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

#Test cases
values_test = [1, 2, 3, 'abc', 3.14, 5]
filtered_ints = filter_integers(values_test)
assert filtered_ints == [1, 2, 3]
values_empty = []
filtered_empty = filter_integers(values_empty)
assert filtered_empty == []
values_list = [1, 2, 3, 'abc', []]
filtered_list = filter_integers(values_list)
assert filtered_list == [1, 2, 3]
values_complex = [1, 2, 3, 'a', (4 + 3j)]
filtered_complex = filter_integers(values_complex)
assert filtered_complex == []
```
This Python code defines a function **filter_integers** that filters a given list of values for only integers. The code also provides several test cases that verify the correctness of the function.