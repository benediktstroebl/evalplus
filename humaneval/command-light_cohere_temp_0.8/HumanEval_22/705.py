```python
from typing import List
def filter_integers(values:
    return [i for i in values if type(i) == int]

# Test
test_values = [1, 2, 3, 'abc', 5, []]
test_result = filter_integers(test_values)
assert test_result == [1, 2, 3]
test_empty_values = [1, 2, 3]
test_result2 = filter_integers(test_empty_values)
assert len(test_result2) == 0
```
The function `filter_integers` accepts a list of values and returns a new list with only integer values from the input. It utilizes a filtering based on the type of each element in the list.

The test cases are provided to ensure the function's correctness.