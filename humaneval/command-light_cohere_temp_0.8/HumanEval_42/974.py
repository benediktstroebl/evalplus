```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result) == [x + 1 for x in l]
    return result

# Test the function
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)
 ```