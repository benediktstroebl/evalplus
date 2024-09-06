```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test cases for get_positive function

# Should return [-1, 2, 3, 5, 6]
get_positive([-1, 2, -4, 5, 6])

# Should return [5, 3, 2, 3, 9, 123]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```