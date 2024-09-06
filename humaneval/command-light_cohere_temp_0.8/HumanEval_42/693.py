```python
def incr_list(lst):
    lst.add(1)
    lst.add(2)
    lst
    lst.add(3)
    lst
    lst.add(4)
    lst
    lst.add(5)
    lst
    lst.add(5)
    lst
    lst

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert incr_list([5, 6, 7]) == [5, 6, 7]
```