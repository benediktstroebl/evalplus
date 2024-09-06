Here is a self-contained Python script that solves the problem of filtering out non-integer values from a list of any python values:
```python
from typing import List

def filter_integers(values:
        [values] = List(values)
        return [i for i in values if isinstance(i, int)]

# Test case 1: Filter integers from a list of strings
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3, "Expected: [3, 14, 5], Actual: {}".format(result)

# Test case 2: Filter integers from a list of numbers
test_numbers = [1, 2, 3, 'abc', {}, []]
result = filter_integers(test_numbers)
assert len(result) == 3, "Expected: [1, 2, 3], Actual: {}".format(result)
```

This script defines a function `filter_integers` that takes a list of any python values as an argument and returns a new list that contains only the integers from the input list. 

The test cases demonstrate how the function behaves when passed different types of lists.