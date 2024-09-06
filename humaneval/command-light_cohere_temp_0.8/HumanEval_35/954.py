```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test cases
test_max_element = [
    """Test suite for max_element function."""
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123, "Max element not found."
    lst2 = [1, 2, 3, -5, 4, 5, -6]
    assert max_element(lst2) == 5, "Max element not found."

# Run the tests
print("Max element test cases passed:")
```