```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_result = filter_integers(test_values)

print("Test Values:", test_values)
print("Test Results:", test_result)

```