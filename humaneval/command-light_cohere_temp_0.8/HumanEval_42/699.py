```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_1 = [1, 2, 3]
test_result = incr_list(test_1)
assert test_result == [2, 3, 4]

# Test case 2
test_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_2)
assert test_result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (odds)
test_3 = [1, 2, 3, 4, 5]
test_result = incr_list(test_3)
assert test_result == [2, 3, 4, 5, 6]
```
This Python code defines a function called `incr_list` that takes a list as an argument and returns a new list with elements incremented by 1. The code includes three test cases to verify the correctness of the `incr_list` function. 
In the first test case, the input list `[1, 2, 3]` is passed to the function, and the expected output is `[2, 3, 4]`. In the second test case, the input list `[5, 3, 5, 2, 3, 3, 9, 0, 123]` is passed, and the expected output is `[6, 4, 6, 3, 4, 4, 4, 10, 1, 124]`. The third test case is designed to validate the behavior of the function with an input list containing odd numbers. The expected output is `[2, 3, 4, 5, 6]`.