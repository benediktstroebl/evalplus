```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list of values
print(filter_integers(['a', 3.14, 5]))  # Output: [5]

# Test case 2: Filter integers from a list of mixed values
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]

# Test case 3: Filter integers from empty list
print(filter_integers([]))  # Output: []
```

The function **`filter_integers`** accepts a list of values as input and uses a list comprehension to filter out any values that are of the integer data type. It adheres to Python's official type hints and is a self-contained solution for the provided problem statement.