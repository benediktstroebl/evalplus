```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test case 1
test_incr_list = [1, 2, 3]
result = incr_list(test_incr_list)
assert len(result) == 3
assert result[0] == 3

# Test case 2
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert len(result) == 13
assert result[10] == 1
```