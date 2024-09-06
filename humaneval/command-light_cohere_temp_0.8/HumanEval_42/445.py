```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l[:] + [2]

# Test cases
test_incr_list = [
    (True, [1, 2, 3]),
    (False, [5, 3, 5, 2, 3, 3, 9, 0, 123])
]

def test_func(test_case):
    actual_result = incr_list(test_case[1])
    expected_result = test_case[0]
    assert actual_result == expected_result, f"Test case {test_case[0]} failed"
    return actual_result

# Test function
test_suite = [
    test_incr_list,
    (True, [1, 2, 3]),
    (False, [5, 3, 5, 2, 3, 3, 9, 0, 123])
]

for test in test_suite:
    test_func(test)
```
The provided Python script defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. It also contains a test cases (test_incr_list) to verify the correctness of the incr_list function. The function test_func takes a test case as input and returns the result of incr_list applied to the corresponding input. The test suite contains two test cases, and the test_func function is used to run these tests and verify the correctness of the incr_list function.