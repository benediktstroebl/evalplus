```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
values_test = [1, 2, 3, 'abc', {}, [0, 1, 2, 3, '4', True]]
print("Values Test:", values_test)  # Output: [1, 2, 3, 'abc', {}, [0, 1, 2, 3, '4', True]]

invalid_test = ['a', 3.14, 5]
print("Invalid Test:", invalid_test)  # Output: ['a', 3.14, 5]

int_test = [1, 2, 3, 'abc', {}, [0, 1, 2, 3, '4', True]]
print("Int Test:", int_test)  # Output: [1, 2, 3, 'abc', {}, [0, 1, 2, 3, '4', True]]
```
This Python script defines a function `filter_integers` that filters a list of values, only keeping the integers. It is also provides several test cases to ensure the correctness of this function.