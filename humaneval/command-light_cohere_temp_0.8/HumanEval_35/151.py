```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with a list of mixed positive and negative numbers
# Make sure the function returns the correct answer
# Test the function with a list of strings (which should have a maximum element of 0)

# Test the function with a list of extreme values
tests = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(tests) == 123

# Test the function with a list of all possible integers
tests = [0] + range(1000)
assert max_element(tests) == 1000

# Test the function with a list of strings
tests = ["hello", "world"]
assert max_element(tests) == 0
```

The code defines a function `max_element` that takes a list as input and returns the maximum element from the list. It also includes a set of tests to ensure the function is working correctly with different types of input.