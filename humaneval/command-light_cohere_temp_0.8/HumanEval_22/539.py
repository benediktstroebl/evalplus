```python
from typing import List
def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, 3, 'abc', 4, 5, (6)]
test_output = filter_integers(test_values)
print(test_output)
```