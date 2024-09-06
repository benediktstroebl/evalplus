```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test_case1))  # Output: [5]
print(filter_integers(values_test_case2))  # Output: [1, 2, 3]
```