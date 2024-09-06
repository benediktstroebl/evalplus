```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l] + [n + 1]
    return result

# Test function
def test_incr_list():
    """Return True if list was successfully incremented."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(lst)
    return result == lst
test_incr_list()  # Should return True
```