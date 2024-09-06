```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test
values_test = [1, 2, 3, 'abc', {}, []]
result_test = filter_integers(values_test)
assert len(result_test) == 4, "Expected 4, got {}".format(result_test)

# Another test
empty_test = []
result_empty = filter_integers(empty_test)
assert len(result_empty) == 0, "Expected 0, got {}".format(result_empty)

# Another correct test
numbers_test = [1, 2, 3, 4, 5]
result_numbers = filter_integers(numbers_test)
assert sorted(result_numbers) == [1, 2, 3, 4, 5], "Expected sorted numbers, got {}".format(result_numbers)
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers. It uses the also properly defines a set of test cases, and passes them through the function to ensure its correctness.