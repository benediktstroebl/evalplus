```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test the function with a list of elements
test_list = [1, 2, 3]
result = incr_list(test_list)
print("Result:", result)

# Test the function with a list of numbers
test_numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_numbers)
print("Result:", result)

# Test the function with a custom tuple
test_tuple = ([1, 2, 3], [4, 5, 6])
result = incr_list(test_tuple)
print("Result:", result)
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The test section demonstrates the unique features of Python — you can create an indented block or a docstring for the test cases using the `test` keyword and pass in the actual values to the `incr_list` function for testing. 

This script is self-contained and can be copied and pasted into a Python environment to run the code.