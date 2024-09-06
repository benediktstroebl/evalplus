```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [i+1 for i in l]
    return l

# Test function to verify the correctness of incr_list
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
```