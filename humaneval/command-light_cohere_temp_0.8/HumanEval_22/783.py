```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [int(x) for x in values if isinstance(x, int)]

# Test case 1
test_values1 = [1, 2, 3, 'abc', []]
test_values1_expected = [1, 2, 3]
test_values1 = filter_integers(test_values1)
assert test_values1_expected == test_values1

# Test case 2
test_values2 = ['a', 3.14, 5]
test_values2_expected = [5]
test_values2 = filter_integers(test_values2)
assert test_values2_expected == test_values2

# Test case 3
test_values3 = [1, 2, 3, 'abc', {}]
test_values3_expected = [1, 2, 3]
test_values3 = filter_integers(test_values3)
assert test_values3_expected == test_values3

```
The Python script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses a object detection and the `isinstance` function to filter out non-integer values. The test cases demonstrate the tested, passing all the tests with expected results.