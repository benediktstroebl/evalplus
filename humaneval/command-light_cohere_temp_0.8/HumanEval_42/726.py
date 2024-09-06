```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    return l

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```