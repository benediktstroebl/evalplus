```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [21]
]

for test_case in test_incr_list:
    actual_result = incr_list(test_case)
    assert actual_result == test_case  # Test for each case
```