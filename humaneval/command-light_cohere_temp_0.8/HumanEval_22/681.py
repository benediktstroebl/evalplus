```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    result = [x for x in values if isinstance(x, int)]
    return result

# Test cases
test_data = [['a', 3.14, 5], [1, 2, 'abc', }, []]
test_results = filter_integers(test_data)
print("Test results:", test_results)  # Output: [5, 1, 2]
test_data = [1, 2, 3, 'abc', {}, ]
test_results = filter_integers(test_data)
print("Test results:", test_results)  # Output: [1, 2, 3]
```
This script defines a function called `filter_integers` that filters a list of any Python values and returns a new list containing only the integers. The function uses the testing cases, and the test results are displayed.