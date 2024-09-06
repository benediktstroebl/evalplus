```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if type(x) == int]

# Test cases
test_cases = [
    [['a', 3.14, 5'], [1, 2, 3, 'abc', {}, []],
    [(1, 2), (3, 'a'), (4, 'b')],
    [True, False, True]
]

for test_case in test_cases:
    actual_output = filter_integers(test_case)
    expected_output = [int(x) for x in test_case]
    assert actual_output == expected_output, f"Test case [{test_case}] failed: {actual_output}"
```