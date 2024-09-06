```python
def incr_list(lst):
    """Return list with elements incremented by 1."""
    return [lst[i]+1 for i in range(len(lst))] 

# Test function
def test_incr_list():
    """Test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert not incr_list([10, 20, 30]) == [10, 20, 30]
```