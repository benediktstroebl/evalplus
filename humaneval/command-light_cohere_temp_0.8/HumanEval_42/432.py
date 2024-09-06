```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test function
def test_incr_list():
    """Return True if list was successfully incremented."""
    lst = [1, 2, 3]
    if incr_list(lst) != lst:
        return False
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    if incr_list(lst) != lst:
        return False
    return True
```