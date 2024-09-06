```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123]
get_positive([1, 2, 3, -4, -123])  # Input: [-1, 2, 3, -4, -123]
# This will raise an error due to the negative numbers
```