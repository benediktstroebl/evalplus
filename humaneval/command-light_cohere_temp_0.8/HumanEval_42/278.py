```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with various input
# Ensure the function works correctly with different types of lists
# Ensure the function works correctly with built-ins lists
test_incr_list = [
    ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]),
    ([], tuple([1, 2, 3])),
    ([6], [1, 2, 3])
]

# Check if the function correctly returns a list with elements incremented by 1
for test_set in test_incr_list:
    actual_set = incr_list(test_set)
    assert len(set()) == len(actual_set)
    for i in range(len(test_set)):
        assert test_set[i] == actual_set[i] + 1
```