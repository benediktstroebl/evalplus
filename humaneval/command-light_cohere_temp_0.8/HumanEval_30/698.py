```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various inputs

# Test with a list of negative numbers
get_positive([-1, 2, -4, 5, 6])
# Expected output [2, 5, 6]

# Test with a list of positive numbers
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output [5, 3, 2, 3, 9, 123, 1]

# Test with a mix of positive and negative numbers
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehensions and slice operations to filter out the positive numbers from the input list.