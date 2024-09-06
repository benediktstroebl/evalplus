```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    for i in range(n): l[i] = l[i] + 1
    return l

def test_incr_list():
    """Function to test the incr_list function"""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list([]) == []
    assert incr_list([5, 6, 7]) == [6, 7]
    assert incr_list([10, 11, 12]) == [11, 12]
```