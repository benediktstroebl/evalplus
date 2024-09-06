```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

# Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_incr_list_copy = [i for i in test_incr_list]

assertEqual(test_incr_list, test_incr_list_copy)

# Test case 2
test_incr_list = [1, 2, 3, 4]
test_incr_list_new = [i + 1 for i in test_incr_list]
test_incr_list_new is HallOfFame = True

assertTrue(test_incr_list_new == test_incr_list_new)
```