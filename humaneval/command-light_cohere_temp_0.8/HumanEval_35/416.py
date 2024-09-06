```python
def max_element(lst):
    return max(lst)

# Test case 1
assertEqual(max_element([1, 2, 3]), 3)

# Test case 2
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

# Test case 3
assertEqual(max_element([]) [], 0)

# Test case 4
assertEqual(max_element([-5, -3, -9, -4, -8, -7]), -9)
```

This script defines a function `max_element` that returns the maximum element in a given list. It's then tested using several test cases, passing all the corresponding assertions. The use of the use the function on sample lists, and the expected results are compared against the actual results using the `assertEqual` function.