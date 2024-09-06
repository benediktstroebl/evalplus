```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases
test_cases = [
    [],
    ['a', 3, 'abc', 5],
    [1, 2, 3, 'abc'],
    [1, 2, 3, 4, 5],
    []
]

for tc in test_cases:
    actual = filter_integers(tc)
    expected = [i for i in tc if type(i) == int]
    assert actual == expected, f"Test case {tc} failed"
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only integers. The test cases demonstrate the value of the function.