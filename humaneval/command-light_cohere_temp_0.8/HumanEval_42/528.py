```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst.append(1)
    return lst

def test_incr_list():
    """Test the incr_list function"""
    lst = [1, 2, 3]
    assert incr_list(lst) == [2, 3, 4]
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(lst) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```