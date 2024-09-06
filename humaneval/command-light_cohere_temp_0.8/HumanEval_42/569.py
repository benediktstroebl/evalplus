```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

# Test function
def test_incr_list():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    test_result = incr_list(test_list)
    print(test_result == [6, 4, 6, 3, 4, 4, 10, 1, 124])
```