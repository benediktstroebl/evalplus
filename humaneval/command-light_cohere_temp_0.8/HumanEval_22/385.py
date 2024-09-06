```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test the function with a list of different data types
values_test = [['a', 3.14, 5], [1, 2, 'abc'], [(), []]

print(filter_integers(values_test))  # Expected output: [5, 1, 2, 'abc']
```

This script defines a function `filter_integers` that filters a list of values to include only the integers. It uses list comprehension and a function `type` to ensure that only integers are returned. The test cases are provided to check the function's correctness.