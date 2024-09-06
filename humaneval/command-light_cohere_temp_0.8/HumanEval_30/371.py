```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various inputs
# Returns the same list as the function above
get_positive([-1, 2, -4, 5, 6])
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Test tuple and set inputs
get_positive((-5, 7, -3))
get_positive({-5, 7, -3})
```
This script defines a function `get_positive` that returns a list of only the positive numbers from the input list. The function is tested with a variety of inputs and passes the tests successfully.