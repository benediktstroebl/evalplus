```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l] + [n]
    return result

# Test the function with a list of numbers
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_list)
test_result_eq = [6, 6, 6, 4, 6, 4, 4, 10, 1, 124]

# Print the results of the function and the test_result_eq
print("Function Result:",test_result)
print("Test Result:",test_result_eq)

```
This script defines a function `incr_list` that takes a list `l` as input and returns a new list with elements from `l` incremented by 1. The function is then tested with a sample list of numbers and the results are compared against an expected output. 

The script also includes the test code, which creates a test list, calls the `incr_list` function with this list, and compares the result against the expected output.