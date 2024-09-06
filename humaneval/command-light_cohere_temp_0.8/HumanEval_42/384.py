```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l] + [n]
    return result

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4] # Should return [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124] # Should return modified list with new values
   

# Test individual cases
def test_individual_cases():
    assert incr_list([5, 3, 5, 2, 3, 3]) == [6, 4, 6, 3, 4] # Should return modified list with new values
    assert incr_list([0, 9, 0]) == [0, 9, 0] # Should return [0, 9, 0]

# Run the full test suite
test_incr_list()
```