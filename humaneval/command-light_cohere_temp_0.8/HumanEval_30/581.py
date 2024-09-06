```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123]
get_positive([])  # Output: []
get_positive([42, -1])  # Output: []

# Test with empty list
get_positive([])  # Output: []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses list comprehension and a condition to filter out the positive numbers. You can test the read this code to see how it works.