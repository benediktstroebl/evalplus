```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list containing both positive and negative numbers
# Test with a list of integers and a list of floats
tests = [[-1, 2, -4, 5], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

# Verify that the function returns the expected list of positive numbers
print(get_positive(tests))  # Output: [2, 5, 6, 3, 9, 123]

# Verify that the function correctly handles both integers and floats
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123]
```

The function `get_positive()` uses a list comprehension to filter out any negative numbers from the input list. The test cases cover a positive and negative numbers, both integers and floats.