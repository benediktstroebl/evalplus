Here is a self-contained Python script that solves the problem of filtering integers from a list of various Python objects:
```python
from typing import List, Any

def filter_integers(values:
    """ Filter given list of any python values for integers and return a new list of int.

    if not isinstance(values, list):
        raise ValueError("Input must be a list")

    new_int_list = [num for num in values if isinstance(num, int)]
    return new_int_list

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3], [4, 5, 6]]
print(filter_integers(values1))  # Output: [1, 2, 3]

values2 = [1, 2, 3, 'a', 4]
print(filter_integers(values2))  # Output: []

values3 = [1, 2, 3, 4, 'abc']
print(filter_integers(values3))  # Output: []
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input list. It uses the also provide some self-contained tests for this function to validate its correctness.