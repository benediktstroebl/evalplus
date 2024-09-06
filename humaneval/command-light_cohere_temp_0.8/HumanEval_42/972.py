```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

def test_incr_list():
    """Test function to check if incr_list works correctly."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This code defines the function `incr_list` that adds 1 to each element in the input list, and passes the test with this function by checking the result against the expected output.