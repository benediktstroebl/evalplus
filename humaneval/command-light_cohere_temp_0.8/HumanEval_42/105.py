```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l] + [n]
    return result

# Test cases
test_incr_list = [
    ( [1, 2, 3], [2, 3, 4 ]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124]),
    ([], [])
]

# Function Call and Test
for test in test_incr_list:
    actual_result = incr_list(test)
    expected_result = test[1]
    assert actual_result == expected_result, f"Test {test[0]} failed."
```