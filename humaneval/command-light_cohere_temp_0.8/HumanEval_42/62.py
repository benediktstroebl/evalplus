```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = []
test_incr_list.add([list([1, 2, 3]))
test_incr_list.add([list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]))

# Loop to run all tests
for test in test_incr_list:
    assert(test == incr_list(test)), "Test failed: " + test"
```