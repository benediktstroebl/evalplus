```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [None]
]

for test in test_incr_list:
    actual = incr_list(test)
    assert actual == [2, 3, 4], f"Failed for {test}"
```
The provided code defines a function incr_list that adds one to the last element of the input list, and tests that the output list equals the expected result for various test cases.