```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2] + [3]
    
def test_incr_list():
    """Test incr_list function."""
    l = [1, 2, 3]
    expected = [2, 3, 4]
    assert incr_list(l) == expected
```