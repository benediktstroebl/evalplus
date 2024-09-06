```python
def incr_list(lst):
    lst[::start:].append(1)
    return lst

def test_incr_list():
    lst = [1, 2, 3]
    incr_list(lst)
    assert len(lst) == 6
    assert lst[0] == 2
    assert lst[1] == 3
    assert lst[2] == 4
    assert lst[3] == 5
    assert lst[4] == 6
    assert lst[5] == 3
    assert len(set(map(str, lst)))) == 1
```