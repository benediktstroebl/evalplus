```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i + 1 for i in l]
    return l

# Test function
def test_incr_list():
    """Test incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([5, 6, 7)))) == 2
    assert incr_list([10, 20, 30, 40]) == [10, 20, 30, 40]

# Driver code
if __name__ == "__main__":
    test_incr_list()
```