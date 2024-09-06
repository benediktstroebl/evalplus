```python
from typing import List
def filter_integers(values:
    returns = List[int]
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [['a', 3.14, 5'], [1, 2, 3, 'abc', {}, []]
]

for test_case in test_cases:
    actual = filter_integers(test_case)
    expected = [5]
    assert actual == expected, f"Test case {test_case} failed."
```