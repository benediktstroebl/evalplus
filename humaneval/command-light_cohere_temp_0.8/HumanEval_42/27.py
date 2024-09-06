```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with sample inputs
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([99, 100, 101])) == 3   # Additional test with different ranges

# Use the function
new_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(new_list)
```