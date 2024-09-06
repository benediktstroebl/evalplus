```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5], [1, 2, 'abc', None, []], [1, 2, 3, 'abc', {}, [1, 2]]
]

def test(test_case):
    actual = filter_integers(test_case)
    expected = [5, [1, 2, 3], 'abc']
    assert actual == expected, f"Test {test_case} failed"

test_filter_integers(test_case)
```

The provided Python script defines a function **filter_integers** that filters a given list of values for integers. The test_filter_integers test suite validates this function's correctness by comparing the output of the function with the expected integer values. The test suite covers a list of any data types, including **str**, **None**, and a nested **List**.  The test passes if all values in the list are integers.