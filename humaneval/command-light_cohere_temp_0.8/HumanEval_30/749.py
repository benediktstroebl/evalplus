```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test cases
get_positive([-1, 2, -4, 5, 6])  # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # [5, 3, 2, 3, 9, 123, 1]
get_positive([])  # []
get_positive([-120])  # [ ]

# Output:
```

This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive integers from the original list. The function uses a simple list comprehension to filter out the positive numbers from the input list, and the test cases demonstrate its functionality for different input scenarios.