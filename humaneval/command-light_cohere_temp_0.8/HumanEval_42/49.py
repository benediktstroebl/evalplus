```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x+1 for x in l]

# Test code to check the correctness of the function
def test_incr_list():
    """Test the incr_list function."""
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    actual = incr_list(lst)
    assert expected == actual
```