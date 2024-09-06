```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Conversely negative numbers)
get_positive([1, 2, 3, -4, -5])
# []
```