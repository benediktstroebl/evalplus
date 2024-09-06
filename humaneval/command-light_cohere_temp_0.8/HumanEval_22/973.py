Here's the code:

```python
from typing import List

def filter_integers(values:
    """ Filter given list only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values1 = [3.14, 5]
test_result1 = filter_integers(test_values1)
assert test_result1 == [5]

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, []]
test_result2 = filter_integers(test_values2)
assert test_result2 == [1, 2, 3]
```

This script defines a function `filter_integers` that accepts a list of values and returns a new list containing only the integers from the input. It uses the Python's `isinstance` function to check if each element in the input list is an integer or not. The test cases provided are used to verify the correctness of the function.