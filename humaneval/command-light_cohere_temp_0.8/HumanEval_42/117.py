```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    ( [1, 2, 3], [2, 3, 4 ] ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
]

for test_case in test_incr_list:
    actual_result = incr_list(test_case)
    assert actual_result == test_case
```