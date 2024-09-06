```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2]

def test_incr_list():
    """Test function to check if incr_list function works as expected."""
    l = [1, 2, 3]
    expected = [2, 3, 4]
    actual = incr_list(l)
    assert expected == actual
```