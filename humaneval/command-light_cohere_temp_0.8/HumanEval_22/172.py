```python
from typing import List

def filter_integers(values:
    """Return list of integers only"""
    result = [x for x in values if isinstance(x, int)]
    return result

# Test cases
test_data = [1, 2, 'three', 3.14, [1, 2, 'abc', 3]]
test_results = filter_integers(test_data)
print("Test Results:", test_results)

# Correct Output
[1, 2, 3, 3. ][: int]
```