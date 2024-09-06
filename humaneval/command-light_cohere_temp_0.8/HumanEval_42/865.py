```python
def incr_list(lst):
    lst[:] = [1, 2, 3]
    return lst

# Tests
def test_incr_list():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([1, 2, 3])
    assert not incr_list([])
    assert not incr_list([10, 20, 30])
```