```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (Should raise IndexError)
try:
    assert incr_list([10])  # Test case should raise IndexError
except AssertionError:
    print("Test case failed!")
```