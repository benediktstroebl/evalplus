```python
from typing import List

def filter_integers(values:
    return [int(x) for x in values if x.isinstance(int)])

# Test cases
test_data = [1, 2, 3, 'abc', {}, [5, 6]]
test_result = filter_integers(test_data)
print(test_result)  # Output: [1, 2, 3, 5, 6]

test_empty = []
test_result_empty = filter_integers(test_empty)
print(test_result_empty)  # Output: []

test_non_integer = ['a', 3.14]
test_result_non_integer = filter_integers(test_non_integer)
print(test_result_non_integer)  # Output: []
```
This script defines a function called `filter_integers` that filters a list of values to include only integers. It provides test data and an empty list as test cases to ensure the function works correctly.