```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test case
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
res = incr_list(test_incr_list)
assert res == [6, 4, 6, 3, 4, 4, 10, 1, 124] # Test if function works
```