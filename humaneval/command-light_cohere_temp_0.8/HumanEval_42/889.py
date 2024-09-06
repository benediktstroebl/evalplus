```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with known good inputs/outputs
for test_case in [(1, [1, 2, 3]), (5, [5, 3, 5, 2, 3, 3])]:
    actual = incr_list(test_case[1])
    expected = test_case[0]
    assert actual == expected, f"AssertionError: {actual} != {expected}"
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The test_case variable contains test cases to check if the function is working correctly. The assert statement checks if the expected outputs match the actual outputs of the function for the given inputs, and an error is raised if the assertions are not satisfied.