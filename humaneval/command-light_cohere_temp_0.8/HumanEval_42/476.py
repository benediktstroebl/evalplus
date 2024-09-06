```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_elements = [x + 1 for x in l]
    return new_elements

# Test suite for the function incr_list
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([55, 33, 88, 11, 66, 83, 90])) == 3
    assert incr_list([]) == []
    assert len(incr_list([1, 2, 3, 4, 5]))) == 5
test_incr_list()
```
The above Python script defines a function `incr_list` that returns a list with elements incremented by 1. It also includes a test suite with a series of assertions to verify the correctness of the `incr_list` function.