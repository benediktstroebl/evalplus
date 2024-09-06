```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]
 
def test_incr_list():
    """Test incr_list function."""
    l = [1, 2, 3]
    assert l == incr_list(l), "Incorrect return value"
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert l == incr_list(l), "Incorrect return value"

# Call test_incr_list to run the test suite."""
test_incr_list()
```