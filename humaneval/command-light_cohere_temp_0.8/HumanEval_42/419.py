```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [0] * (n+1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i-1] + 1
    return result

# Test the function with different list inputs
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_list)
print("Test list:", test_list)
print("Test result:", test_result)

# Validate the function behavior with different scenarios
valid_list = [1, 2, 3]
invalid_list = [5, 3, 5]
invalid_result = incr_list(invalid_list)
print("\nValid list:", valid_list)
print("\nInvalid list:", invalid_list)
print("\nValid result:", valid_result)
print("\nInvalid result:", invalid_result)
```
This Python script defines a function called `incr_list` that takes a single argument, `l`, which is an input list. It then creates a copy of the input list, with the same elements but incremented by 1. The function then returns this new list, which has the elements of the original list incremented by 1.

The script also includes a series of tests for the `incr_list` function. It first tests a test the function with a test list and prints the original test list and the result. Then, it validates the function's behavior with different scenarios: a valid list and an invalid list, and finally, it prints the valid and invalid results for these inputs.