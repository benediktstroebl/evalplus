```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = [3.14, 'abc', 5]
print("Case 1: ", end = "")
print(filter_integers(values1))

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print("Case 2: ", end = "")
print(filter_integers(values2))

# Test case 3
values3 = [1, 2, 3]
print("Case 3: ", end = "")
print(filter_integers(values3))
```
The above Python script defines a function `filter_integers` that filters a given list of values for only integers. The function uses the filter built-in Python function for the same purpose. The test cases demonstrate the use of the `filter_integers` function to filter the given lists of values.