```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [
    [1, 2, 3], ['abc', 3, 'five'], [1, 2, 'three']
]

test_cases = [
    (test_values, 'integer'),
    (test_values, 'not integer')
]

for case in test_cases:
    actual = filter_integers(case[0])
    expected = case[1]
    print(f"Case: {actual}, {expected} - {'Found integers'}")
```