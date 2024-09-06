```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of values
get_positive([-1, 2, -4, 5, 6])
# [2, 5, 6]

# Test with a mix of numbers and strings
get_positive([5, 3, -5, 2, -3, 'Hello'])
# [2, 3, 5, 'Hello']

# Test with a list of integers
get_positive([1, 2, 3, 4, 5])
# [1, 2, 3, 4]

# Test with a empty list
get_positive []
# []
```