```python
def incr_list(lst):
    lst[:] = [lst[-1] + 1]
    return lst

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
```
This code defines a function incr_list that takes in a list lst and increments each element by 1. It then returns the notice that this function is self-contained as it can be used without the need for any external functions or modules.