```python
def incr_list(lst):
    lst[:] = [lst[-1]+1] + lst
    return lst

# Test cases for incr_list function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert incr_list([10, 100]) == [101, 100]
    assert incr_list([5, 10, 100, 101]) == [106, 101, 100, 101]
```