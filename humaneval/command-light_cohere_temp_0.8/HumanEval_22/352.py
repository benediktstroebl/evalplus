```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Simple list of integers
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: List of mixed data types
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3: Empty list
print(filter_integers([]))      # []

# Test case 4: Single element
print(filter_integers(5))       # [5]
```
This script defines a function `filter_integers` that filters a given list of values based on whether each element is an instance of the `int` class. The function returns a necessary list of integers.  The tests demonstrate the multiple scenarios for the function.