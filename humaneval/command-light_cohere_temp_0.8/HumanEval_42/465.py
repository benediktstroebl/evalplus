```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l

def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
```
The test_incr_list() function tests the correctness of the incr_list() function by passing the correct input and checking if the returned value matches the expected output. This ensures that the index will be incremented by 1 correctly.