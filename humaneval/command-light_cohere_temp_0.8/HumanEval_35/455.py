```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
assertEqual(max_element([1, 2, 3]), 3)

# Test case 2
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

# Test case 3 (lists with different data types)
assertEqual(max_element([[1, 2, 3], 4, 5]) , 5)

# Test case 4 (empty list)
assertEqual(max_element([]) , [])
```

The provided code defines a Python function `max_element` that takes a single argument `l`, which is expected to be a list. It then uses the the`max` function from the built-in `math` module to find and return the maximum element in the list.

The function is then tested with four different input scenarios, and the results are compared with the expected maximum element using the `assertEqual` function.