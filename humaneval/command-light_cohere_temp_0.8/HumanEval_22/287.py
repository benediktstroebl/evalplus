Here is a self-contained Python function that solves the problem of filtering integers from a list of various values:
```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

for test_case in test_cases:
    actual = filter_integers(test_case)
    assert all(actual == [x for x in test_case if isinstance(x, int)])
```

This function is self-contained and can be used to filter a list of any values, including strings, objects, and other data types, and only returns the list of integers. The test cases provided validate the are designed to test the correctness of the `filter_integers` function.