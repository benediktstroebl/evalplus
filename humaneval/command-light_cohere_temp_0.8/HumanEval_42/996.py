```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [x + 1 for x in l]
    return result

def test_incr_list():
    """Return list with elements decremented by 1"""
    return [x - 1 for x in [1, 2, 3, 4, 5]]

result = incr_list([1, 2, 3])
assert len(result) == 3   # Should be [2, 3, 4]
result = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert len(result) == 7   # Should be [6, 4, 6, 3, 4, 4, 10]

result = test_incr_list()
assert len(result) == 7   # Should be [6, 4, 6, 3, 4, 4, 10]
```