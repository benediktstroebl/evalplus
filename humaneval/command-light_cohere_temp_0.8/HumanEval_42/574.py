```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    lst[:] = [lst[-1] + 1]
    return lst

# Test function to check incr_list function
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(lst)
    assert result == [6, 3, 6, 4, 6, 4, 4, 10, 1]
```