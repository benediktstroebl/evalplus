```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3, "Test case 1 failed"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3, "Test case 2 failed"

# Test case 3
values3 = [1, 2, 3, 'abc']
result3 = filter_integers(values3)
assert len(result3) == 3, "Test case 3 failed"
```
This Python code defines a function `filter_integers` that filters a given list for only integer elements. It uses a universal new `typing` module to handle Python `Any` types. The function iterates through each element in the list and checks if it's an instance of `int`. It returns a new list with only the integer elements. The code includes three test cases to verify the correctness of the `filter_integers` function.