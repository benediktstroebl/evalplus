```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [x + 1 for x in l]
    return l[:n]

# Test function
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(test_list)
    assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Run the test function to see the output in the console
test_incr_list()
```