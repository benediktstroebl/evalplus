```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
print(filter_integers(values_test_case1))  # Expected output: [5]

values_test_case2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test_case2))  # Expected output: [1, 2, 3]
```

This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the particular int as the filter function to achieve this.