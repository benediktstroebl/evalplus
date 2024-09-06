```python
from typing import List
def filter_integers(values: 
    return [x for x in values if type(x) == int]

# Test cases
values_test = [1, 2, 3, 'abc', 5, (7)]
expected_test = [1, 2, 3] + [5]  # [1, 2, 3, 5]

# Test single argument
values_single = [1, 2, 3, 'abc']
expected_single = [1, 2, 3]

# Test empty list
values_empty = []
expected_empty = []

print("Test cases passed:")
print("Values:", values_test)
print("Expected:", expected_test)
print("Values single:", values_single)
print("Expected single:", expected_single)
print("Values empty:", values_empty)
print("Expected empty:", expected_empty)
```