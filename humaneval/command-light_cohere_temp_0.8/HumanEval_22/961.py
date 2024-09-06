```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers."""
    return [num for num in values if isinstance(num, int)]

# Test case 1
test_values1 = [3.14, 'a', 5]
test_values1_filtered = filter_integers(test_values1)
assert test_values1_filtered == [3, 5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, [0])
test_values2_filtered = filter_integers(test_values2)
assert test_values2_filtered == [1, 2, 3]

# Test case 3
test_values3 = [True, False, 4, 5, 6]
test_values3_filtered = filter_integers(test_values3)
assert test_values3_filtered == [4, 5, 6]
```
This Python code defines a function named filter_integers that filters a given list of values based on their data type. The function takes a values as an parameter and returns a new list containing only the integers from the input list. This code uses the time to test the function's correctness with three different test cases, and the results are compared against the expected values. The test cases cover various scenarios, such as non-integer values, values of different data types, and mixed data types.