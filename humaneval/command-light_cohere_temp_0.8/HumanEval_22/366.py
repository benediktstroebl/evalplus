```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases for function usage
test_filter_integers = [
    [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []],
    [1, 2, 3], [100, 200, 300], ['foo', 'bar']
]

for test in test_filter_integers:
    actual = filter_integers(test)
    assert actual == test, f"Failed: {actual} != {test}"
```
This code defines a function `filter_integers` that filters a list of values to include only integers. The `test_filter_integers` list is a set of test cases, which are lists of values. Each test case is then passed to the `filter_integers` function and is expected to return a list of integers. The function is then tested using the `assert` function to ensure the correctness of its output.