```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x+1 for x in l]

# Test function
def test_incr_list():
    test_list=[1, 2, 3]
    expected=[2, 3, 4]
    got=[x+1 for x in test_list]
    assert expected == got
```