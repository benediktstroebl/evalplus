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
        ([10, 1, 2], "should return list with elements incremented by 1"),
    )
]

# Function call and results
for case in test_incr_list:
    actual_result = incr_list(case)
    assert actual_result == case
```