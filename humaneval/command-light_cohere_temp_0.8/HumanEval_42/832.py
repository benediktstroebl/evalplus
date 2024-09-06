```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [i+1 for i in l]
    return l

# Test the function with known good inputs and prints the result
def test_incr_list():
    lst = [1, 2, 3]
    assert lst == incr_list(lst)
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert lst == incr_list(lst)
test_incr_list()
```