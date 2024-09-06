```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with various input
def test_incr_list():
    # Test list with existing elements
    test_list = [1, 2, 3]
    result = incr_list(test_list)
    assert all(result == [2, 3, 4])
    # Test list with zero initial value
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(test_list)
    assert all(result == [6, 4, 6, 3, 4, 4, 10, 1, 124])
```
The code defines a function `incr_list` that increments each element of a list by 1 and returns the updated list. It also includes a test_incr_list, which provides test cases for the function, ensuring that the result is correct for various input scenarios.