```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test function
def test_incr_list():
    """Return True if incr_list function works correctly."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(lst)
    if result == lst:
        return True
    else:
        return False
```