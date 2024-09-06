```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Negative list)
get_positive([-2, -5, -8, -1, -100])
# []
```