```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(result) >= n // 2
    assert all(result[i] == i + 1 for i in range(n))
    return result

# Test the function with various lists
test_incr_list = incr_list
test_incr_list([1, 2, 3])
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
```