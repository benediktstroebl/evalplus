```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

# Test the function
def test_incr_list():
    # Test list with some values
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(test_list)
    assert result == expected
```