```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output: [5, 3, 2, 3, 9, 123]

# Test case 3
get_positive([])
# Expected output: []

# Test case 4
get_positive([12, -23, 43, -56])
# Expected output: []
```

This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. It utilizes list comprehensions to filter out the positive elements while checking if each element is non-negative, providing a clean and self-contained solution for the given problem.