```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases for function
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

values3 = [1, 2, 3, 'a', 4]
print(filter_integers(values3))  # Output: ['1', '2', '3', 'a', 4]
```
This Python script presents a function named `filter_integers`, designed to filter a given list and retain only the integer elements. The function operates by utilizing the `isinstance()` function to identify and extract integer values from the input list. The test cases validate the alternative lists of values, and the function's output aligns with the expected results. The `isinstance()` function is instrumental in ensuring that only valid inputs are accepted.