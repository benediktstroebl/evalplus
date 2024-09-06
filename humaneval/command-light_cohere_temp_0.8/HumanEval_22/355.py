```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test
test_values = [1, 2, 3, 'abc', [1, 2, 3], {}]
test_result = filter_integers(test_values)
print(test_result)  # Output: [1, 2, 3]
```