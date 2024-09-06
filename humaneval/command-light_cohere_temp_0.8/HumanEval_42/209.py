```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    assert(all(i <= n for i in l)), "Invalid list, all indices should be less than length!"
    return l

# Test the function with various inputs
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)
```