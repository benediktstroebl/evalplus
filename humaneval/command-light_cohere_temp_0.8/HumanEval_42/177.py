```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = []
test_incr_list.push_back([1, 2, 3])
test_incr_list.push_back([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])

# Function call and results
assert incr_list(test_incr_list) == test_incr_list[1:]
assert test_incr_list[2][0] == 4
assert test_incr_list[3][0] == 6
assert test_incr_list[4][0] == 10
assert test_incr_list[5][0] == 1
```