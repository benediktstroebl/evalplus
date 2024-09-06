```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test the function with a list of inputs
def test_incr_list():
    test_list = [5, 3, 2, 1]
    expected = [6, 4, 3, 2]
    result = incr_list(test_list)
    assert expected == result
```