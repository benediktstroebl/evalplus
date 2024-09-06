```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([5, -5, 5, -5]))
# Output: [5, 5]

# Test case 4
print(get_positive([2, 2, -10, 0, 2, -2, -5, -3, -5]))
# Output: [2, 2, -5, 0]
```

The function `get_positive` takes a list as input and returns a new list containing only the positive numbers from the original list. 

This function can be easily incorporated into any Python script and used to solve the problem of extracting only positive numbers from a list.