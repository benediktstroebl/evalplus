```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    return result

# Test case 1: Basic list increment
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    assert list(incr_list(test_list)) == expected

# Test case 2: List with reusable element
    test_list = [5, 3, 5, 2, 3, 3]
    expected = [6, 4, 6, 3, 4, 4, 10, 1]
    assert list(incr_list(test_list)) == expected

# Test case 3: List with different starting element
    test_list = [0, 1, 2, 3]
    expected = [1, 2, 3]
    assert list(incr_list(test_list)) == expected

# Test case 4: List with negative increment
    test_list = [1, 2, 3]
    expected = [1, 2, 3]
    assert list(incr_list(test_list, -1)) == expected
```