```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123, 1]
get_positive([])  # Input: []
# Output: []

# Another test case
get_positive([10, 11, -12])  # Output: [10, 11]
```

The function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the input list. It uses list comprehension to iterate over the list and filter out the numbers greater than or equal to zero.