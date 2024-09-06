```python
from typing import List

def filter_integers(values:
    return [int(el) for el in values if type(el) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc'], [1, 2, 3], [(), []]

test_cases = [test_values, test_values[::-1]]

for test_val, expected in test_cases:
    actual = filter_integers(test_val)
    assert actual == expected, f"Unexpected result: {actual}, expected: {expected}"
```