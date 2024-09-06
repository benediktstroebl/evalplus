```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test drive
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert len(result) == 12
assert all([i for i in result]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```