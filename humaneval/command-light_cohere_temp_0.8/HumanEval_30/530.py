```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1: This should return [2, 5, 6]
get_positive([-1, 2, -4, 5, 6])

# Test case 2: This should return [3, 5, 2, 3, 9, 123]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Test case 3: This should raise ValueError with an appropriate error message
get_positive([-illery-5])
```