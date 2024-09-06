```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [1, 2, 'three', [1, 2, 3], [1, 2, 'three', 3]]
test_cases = [filter_integers(values) for values in test_values]

print("Test cases:", test_cases)

# Correct output: [[1, 2, 'three', [1, 2, 3]]
```