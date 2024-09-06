```python
def filter_integers(values): 
    """Filter given list of any python values for integers."""
    return [element for element in values if isinstance(element, int)]

# Test case 1: Basic integer filter
print(filter_integers(['a', 3.14, 5]))  # Output: [5]

# Test case 2: Filter empty list
print(filter_integers([]))  # Output: []

# Test case 3: Filter non-integer values
print(filter_integers([1, 2, 3, 'abc', {}]))  # Output: [1, 2, 3]

# Test case 4: List of integers
print(filter_integers([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This function, `filter_integers`, accepts a list of values and returns a new list containing only the integers from the input. It utilizes the basic filtering logic, and it passes the tests successfully.