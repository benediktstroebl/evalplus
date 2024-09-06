```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
import pytest

pytest.org_get_positive([0, 2, -3, -5, -2, -8, -6, -4, -1]))
```
The function `get_positive` returns a list containing only positive numbers from the input list. The test cases demonstrate that the expected output of the function for different input scenarios.