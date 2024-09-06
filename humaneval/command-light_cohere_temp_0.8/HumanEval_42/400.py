```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]
 
def test_incr_list():
    """Test function for incr_list."""
    l = [1, 2, 3]
    assert incr_list(l) == [2, 3, 4]
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(l) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```