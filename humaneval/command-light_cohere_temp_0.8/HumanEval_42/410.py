```python
def incr_list(lst):
    lst[::] = lst[-1] + 1
    return lst

# Test
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 20, 30]))) == 0  # This should be true
    assert incr_list([]) == []
```
The code defines a function incr_list that takes in a list lst and increments each element by 1. The test_incr_list function then passes various tests to the incr_list function, which should return the expected results for the given inputs.