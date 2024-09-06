```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test the function with some examples
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([55, 45, 60, 78, 91]) # Should remain unchanged
    assert incr_list([]) == []
test_incr_list()
```