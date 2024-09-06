```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases
test_values = [1, 2, 3, 'abc', {}, [1, 2, 'three']]
test_cases = [filter_integers, lambda x: type(x) == int]

for test_func, test_values in test_cases:
    assert test_func(test_values) == test_values
```