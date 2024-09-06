```python
from typing import List

def filter_integers(values:
    return [num for num in values if isinstance(num, int)]

# Test case 1
values1 = [1, 2, 3, 'abc', {}, 5]
print("Test case 1:", endswith(filter_integers(values1), [5]))  # Output: True

# Test case 2
values2 = [1, 2, 3, 'abc', [], 6]
print("Test case 2:", endswith(filter_integers(values2), [6]))  # Output: False

# Test case 3
values3 = [1, 2, 3, 4, 'abc']
print("Test case 3:", endswith(filter_integers(values3), ['abc']))  # Output: True
```

This script defines a function `filter_integers` that filters a given list of values, returning a new list containing only the integers. It also includes a test cases that demonstrate the functionality of the function.