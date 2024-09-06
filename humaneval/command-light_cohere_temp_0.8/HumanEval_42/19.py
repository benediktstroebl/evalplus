```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test case 1
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = incr_list(test_incr_list)
assert list(result1) == [6, 3, 6, 4, 6, 4, 10, 1, 124]

# Test case 2
test_incr_list2 = [5, 2, 3]
result2 = incr_list(test_incr_list2)
assert list(result2) == [6, 3, 6]

# Test case 3
test_incr_list3 = [0, 1, 2, 3]
result3 = incr_list(test_incr_list3)
assert list(result3) == [1, 2, 3]

print("All tests passed!")
```