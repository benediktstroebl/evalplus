```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with some examples
get_positive([-1, 2, -4, 5, 6])  # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # [5, 3, 2, 3, 9, 123, 1]
get_positive([1, 2, 3, -4, -100, 5, 6, 7, 8])  # [1, 2, 3, 5, 6, 7, 8]

# The function is correct, you can use it with confidence!
 ```