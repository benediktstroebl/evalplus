```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

# Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_res = incr_list(test_incr_list)
assert test_incr_list_res == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 2
test_2 = [1, 2, 3, 4, 5]
test_2_res = incr_list(test_2)
assert test_2_res == [2, 3, 5, 5, 6, 7]

# Test case 3
test_3 = [1, 2, 3, 100]
test_3_res = incr_list(test_3)
assert test_3_res == [2, 3, 101, 102]
```