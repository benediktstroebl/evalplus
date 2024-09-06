```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [0]

def test_incr_list():
    """Test incr_list function with sample input."""
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(l) == [6, 3, 6, 4, 6, 4, 10, 1, 124]
```