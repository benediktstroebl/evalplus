```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a sample input
test_values = [1, 2, 3, 'abc', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 6  # Check the length of the result is as expected
assert all(isinstance(x, int) for x in result)  # Check each element is an integer

# Test the function again with a different list
test_list = [1, 2, 3, 'a', 4, 5, 'b']
result_second = filter_integers(test_list)
assert len(result_second) == 6  # Check the length of the result is the same as the first test
```
This code defines a function called `filter_integers` that takes a list of values as an argument and returns a new list that contains only the integers from the input list. The code also tests the test the function with two different lists of values, and the expected output is 6 ( integers ) and all are integers.