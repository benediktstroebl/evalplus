```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    (
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ([10, 11],),
    )
]

# Function test
def test_func(test_cases):
    for idx, test_case in enumerate(test_cases, start=1):
        lst = list(test_case)
        expected = [x + 1 for x in lst]
        got = incr_list(lst)
        assert got == expected, f"Case {idx} failed: {got} != {expected}"

# Run the tests
test_incr_list(test_incr_list)
 ``` 
This code defines a function `incr_list` that returns a list with elements incremented by 1. It also provides a testing for this function using the `test_func` which takes a list of test cases. The test case iterates through the list of test cases, where each case is a list of values, and each element is expected to be incremented by 1. The test then iterates through the list, and for each element in the test case, it creates a new list with the same elements but incremented by 1, and compares the two lists. Finally, it uses the assertions in the `test_func` to check if the output of `incr_list` matches the expected output.