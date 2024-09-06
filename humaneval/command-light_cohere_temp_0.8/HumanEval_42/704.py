```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert not incr_list([5, 6, 7]) == [5, 6, 7]
```
The incr_list function takes a list as input and returns a new list with each element incremented by 1. The test_incr_list function contains several tests to verify the correctness of the incr_list function.