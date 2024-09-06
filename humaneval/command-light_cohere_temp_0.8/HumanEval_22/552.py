```python
from typing import List

def filter_integers(values:
    return [num for num in values if type(num) == int]

# Test case 1
values1 = [3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 2, "Filtering failed"

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3, "Filtering failed"

# Test case 3
values3 = [1, 2, 3]
result3 = filter_integers(values3)
assert len(result3) == 3, "Filtering failed"
```