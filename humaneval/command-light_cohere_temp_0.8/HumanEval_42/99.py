```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    return [lst[i]+1 for i in range(len(lst))]

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([100, 200, 300])) == 3
    assert incr_list([]) == []
```