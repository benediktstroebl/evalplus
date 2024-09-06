```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values_test_case1))  # Output: [5]
print(filter_integers(values_test_case2))  # Output: [1, 2, 3]
```
This Python script defines a function called `filter_integers` that filters a given list of any Python values for integers. The function iterates through each element in the list and checks if the element is an instance of the `int` class. The test cases demonstrate the actual outputs.