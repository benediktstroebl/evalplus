```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It utilizes Python's list comprehension feature along with the `isinstance()` function to check if each element in the input list is an instance of the `int` class, and accordingly, filters out non-integer values. 

To ensure the functionality of the solution, here are some example tests that can be conducted to validate the accuracy of the `filter_integers` function:
```python
# Test with a sample list of values containing integers and non-integers
sample_values = [1, 2, '3', 4, 'abc', 5, 6.0]
expected_result = [1, 4, 5]

actual_result = filter_integers(sample_values)

# Test if the function filters out only integers
assert actual_result == expected_result
```

```python
# Test with a sample list containing only non-integer values
sample_values = ['a', 'b', 'c', 'd', 'e']
expected_result = []

actual_result = filter_integers(sample_values)

# Test if the function returns an empty list when no integers are present
assert actual_result == expected_result
```

These tests cover scenarios both when there are integers present in the list and when there are only non-integer values. 

The `filter_integers` function ensures only integers are filtered out from the list when they are present, and returns an empty list when no integers are encountered.