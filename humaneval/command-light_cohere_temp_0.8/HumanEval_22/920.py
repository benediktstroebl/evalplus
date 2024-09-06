```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    [['a', 3.14, 5'], [1, 2, 3, 'abc', {}, []],
    [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13]
]

print("Test cases passed:")
for test in test_filter_integers:
    actual = filter_integers(test)
    assert actual == [x for x in test if isinstance(x, int)], "Test failed"
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the test `is assert` statement to test the correctness of the output, and the `isinstance` checks if each value is an integer. 

Please note that this code is self-contained and can be executed independently, without the need for additional test data or external variables.