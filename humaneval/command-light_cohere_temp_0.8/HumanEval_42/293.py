```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    (([1, 2, 3],), "Should return [2, 3, 4]"),
    (([5, 3, 5],), "Should return [6, 4, 6]"),
    (([10, 0, 123],), "Should return [10, 1, 124]"),
]

# Test execution
for test in test_incr_list:
    actual_result = incr_list(test[0])
    assert actual_result == test[1], f"Failed: {test[0]} -> {test[1]} -> {actual_result}"
```

This Python script defines a function `incr_list` that returns a new list with elements incremented by 1. The function takes an input list `l` as an argument and creates a new list by adding 1 to each element in the input list. The test cases provide various input lists and expected output, and the `assert` statements are used to verify if the function is working correctly for each test case. 

This script is a self-contained way to solve the problem and validate the results.