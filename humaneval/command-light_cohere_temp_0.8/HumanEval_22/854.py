```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = [['a', 3.14, 5]
print(filter_integers(test_values))  # [5]

# Test case 2
test_data = [1, 2, 3, 'abc', {}, [1, 2, 3])
print(filter_integers(test_data))  # [1, 2, 3]
```
This script defines a function `filter_integers` that filters a given list of values, ensuring only the integers are retained. It uses a particular data types and other data-structures to pass all the test cases.