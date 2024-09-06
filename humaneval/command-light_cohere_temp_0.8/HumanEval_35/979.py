```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [list(range(1, 10000)),
    [],
    [1, 3],
    [-5, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [123, 2, 3, -32]
]

for test_case in test_max_element:
    actual_result = max_element(test_case)
    assert actual_result == max(test_case), "Test case failed: " + test_case"
```

This code defines a Python function `max_element` that takes a list as input and returns the maximum element from the list. The test cases are a list of test scenarios, and each test case contains a list that is passed to the `max_element` function. The `assert` statement is used to verify if the result of `max_element` is indeed the maximum element of the corresponding list, which helps ensure the correctness of the function.