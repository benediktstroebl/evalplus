```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([5, 6, 7])  # No change expected, 2 is not in the list.
``` 
This Python script defines a function `incr_list` that returns a list with elements incremented by 1, and a test function `test_incr_list` that checks the correctness of the `incr_list` function using various input lists.