```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [x+1 for x in l]
    return l

# Test case 1
test_cases = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
]

for test in test_cases:
    result = incr_list(test)
    assert result == [2, 3, 4]   # Should be [6, 4, 6] in this case

# Test case 2
test_cases = [
    [1, 2, 3, 4, 5],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
]

for test in test_cases:
    result = incr_list(test)
    assert result == [6, 4, 6]   # Should be [6, 4, 6] in this case
```
The above Python script defines a function `incr_list` that takes a list as input and returns a list with elements incremented by 1. The test cases are defined to ensure that the function works as expected. The test cases are created using a list of lists, and the `assert` statement is used to verify if the `incr_list` function produces the correct output for each test case.