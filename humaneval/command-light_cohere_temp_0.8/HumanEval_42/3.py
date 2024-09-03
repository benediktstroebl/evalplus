```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test case 1: Simple increment
test_incr_list = incr_list([1, 2, 3])
assert len(test_incr_list) == 3
assert test_incr_list[0] == 1
assert test_incr_list[1] == 2
assert test_incr_list[2] == 3

# Test case 2: Empty list
test_empty_incr = incr_list([])
assert len(test_empty_incr) == 0

# Test case 3: List with duplicate elements
test_list_with_duplicates = [5, 3, 5, 2, 3, 3]
test_list_with_duplicates_incr = incr_list(test_list_with_duplicates)
assert len(test_list_with_duplicates_incr) == 4
assert test_list_with_duplicates_incr[0] == 5
assert test_list_with_duplicates_incr[1] == 3
assert test_list_with_duplicates_incr[2] == 2
assert test_list_with_duplicates_incr[3] == 3
```
The Python function `incr_list` takes a list `l` as an argument and returns a new list with elements incremented by 1. The test cases aim to check the functionality of the `incr_list` function by passing various input lists and asserting that the output lists are as expected.