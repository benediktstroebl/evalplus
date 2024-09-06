```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [
    [1, 2, 3, 'abc', 5],
    [],
    [3, 14],
    [123, 456, 789],
    ['foo', 2],
]

test_cases = [
    lambda values: filter_integers(values) == [1, 2, 3, 5],  # Integers only
    lambda values: filter_integers(values) == [123, 456, 789],  # Integers and non-integer
    lambda values: filter_integers(values) == ['abc', 2, 'foo'],  # Non-integer and integers
    lambda values: not([x for x in values if isinstance(x, int)]) == [],  # No integers
]

# Run the test cases
for test_func, expected in zip(test_cases, [test_values[0], test_values[1], ...]):
    assert test_func(test_values) == expected
 ```

This script defines a function `filter_integers` that filters a list to include only integers. It also includes a test cases with a list of values and `filter_integers` function to test its behavior. The test cases check for different scenarios, such as having only integers, only non-integers, both integers and non-integers, and no integers. The script then runs all the test cases and uses the `assert` function to check if the `filter_integers` function returns the correct result for each test case.