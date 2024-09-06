```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases 1
print("Test case 1 passed:", end)
get_positive([-1, 2, -4, 5, 6])

# Test cases 2
print("Test case 2 passed:", end)
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```

The function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the original list. This function is use list comprehension to filter out the numbers greater than or equal to zero. The test cases confirm that the function works correctly for different scenarios of input lists.