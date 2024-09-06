```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n + 1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with various input
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_data)
print(test_result)
``` 
This code defines a function `incr_list` that performs the increment operation on a given list, producing a new list with elements incremented by 1. The test_data list is provided to test the function, and the function is called with this list. The output will display the expected result for the test case.