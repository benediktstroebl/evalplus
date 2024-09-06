```python
from typing import List
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert result_test1 == [5], "Test case 1 failed: Expected [5], got {}".format(result_test1)

# Test case 2: Filter integers from a generator expression
values_test2 = 1, 2, 3, 'abc', {}, []
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3], "Test case 2 failed: Expected [1, 2, 3], got {}".format(result_test2)

# Test case 3: Filter integers from a list with other data types
values_test3 = [1, 2, 3, 'abc', (), [0]]
result_test3 = filter_integers(values_test3)
assert result_test3 == [1, 2, 3], "Test case 3 failed: Expected [1, 2, 3], got {}".format(result_test3)
```

This Python code provides a self-contained function called `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the input. The function uses the specific type checks to ensure it only filters integers, passing all corresponding tests.