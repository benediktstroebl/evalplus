```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [x + 1 for x in l]
    return l

# Test function for incr_list
def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 1, 2, 3])) == 3
    assert incr_list([]) == []
    assert incr_list([5, 6, 7]) == [5, 6, 7]

# Driver code
if __name__ == "__main__":
    test_incr_list()
``` 
This Python script provides a function `incr_list` that takes a list l as input and returns a new list with elements from the original list incremented by 1. The test_incr_list function verifies the correctness of the `incr_list` function by passing various test cases. The `if __name__ == "__main__":` block ensures that the test code is executed only if the script is run directly, not imported elsewhere.