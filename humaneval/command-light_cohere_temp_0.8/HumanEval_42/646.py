```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    return result

# Test the function with a sample input
test_input = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_input)
test_eq = [6, 4, 6, 3, 4, 4, 10, 1, 124]

if not test_eq == test_result:
    raise ValueError("Test failed")

# Test the function again with different input
test_input2 = [5, 3, 9, 2, 98, 3]
test_result2 = incr_list(test_input2)
test_eq2 = [6, 9, 6, 100, 3]

if not test_eq2 == test_result2:
    raise ValueError("Another test failed")
```
The function `incr_list` in this version is self-contained and takes a single argument, `l`, which is an input list. It creates a result list by adding 1 to each element in `l`, and then returns the result list. The test code section runs the test with a sample input, checks that the function returns the right output for that input, and then runs additional tests to ensure that the function behaves correctly with various inputs.