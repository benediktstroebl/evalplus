```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 3, 'abc', (])  # Int containing string, empty tuple, invalid data
result_test = filter_integers(values_test)
assert all(result_test) == [1, 2, 3]

empty_list_test = []  # Empty list
result_empty_test = filter_integers(empty_list_test)
assert result_empty_test == []

large_number_test = 1234  # Integer value larger than 1
result_large = filter_integers(large_number_test)
assert all(result_large) == [1234]
```
This code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integer elements from the original list. It also provides a test cases to ensure the function is working as expected with different inputs.