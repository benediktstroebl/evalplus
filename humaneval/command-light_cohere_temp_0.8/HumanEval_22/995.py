```python
def filter_integers(values):
    """ Filter given list for only integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, '123', [4, 5], 6]
print(filter_integers(values3))  # Output: [1, 2, 3, '123', 4, 5, 6]
```

This function `filter_integers` takes a list of values as an argument and returns a new list containing only the integers from the input list. It uses the `is filtering for integers` is self-contained, and it can be easily used with various lists of values.

Note that it's important to properly define the function and provide the appropriate input tests to ensure the function's correctness.