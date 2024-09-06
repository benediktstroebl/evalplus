Here is a Python script that solves the problem of filtering integers from a list of various data types:
```python
from typing import List, Any

def filter_integers(values):
    # Filtering integers from the input list
    return [num for num in values if isinstance(num, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_results = [filter_integers(values) for values in test_values]

print(test_results)
```

This script provides a self-contained function `filter_integers` that takes a list of values and returns a new list containing only the integers from the original list. The function uses the Python's `isinstance()` function to check if each value in the list is an integer, and filters them out using a list comprehension. The test cases demonstrate how the the function works correctly with a variety of data types.