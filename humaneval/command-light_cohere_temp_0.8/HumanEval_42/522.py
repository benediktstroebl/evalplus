```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test function
def test_incr_list():
    l = [1, 2, 3]
    assert l == [2, 3, 4]  # Test 1
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert l == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # Test 2 - ok
    return l

# Driver code
if __name__ == "__main__":
    # Test function
    test_incr_list()
    print("Test passed")
```