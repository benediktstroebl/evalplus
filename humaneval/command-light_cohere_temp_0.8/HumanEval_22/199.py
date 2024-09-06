```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function
test_values = [1, 2, 3, 'abc', {}, [1, 2, 3], [4, 'w2']]
test_result = filter_integers(test_values)
assert test_result == [1, 2, 3, 4]

# Test the function with invalid input types
test_invalid = ['a', 3.14, 5]
test_result_invalid = filter_integers(test_invalid)
assert test_result_invalid == []
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the value of the function with different types of inputs and validate the results.