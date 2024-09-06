```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3, "Test case 1 failed"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3, "Test case 2 failed"

# Test case 3
values3 = [1, 2, 3, [4, 5], 6]
result3 = filter_integers(values3)
assert len(result3) == 4, "Test case 3 failed"

print("All tests passed!")
```