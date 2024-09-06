```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test function
def test_incr_list():
    """Return True if l is list and all elements are equal to 1."""
    return isinstance(incr_list(test_list()), list) and all(map(int, l)) == [1])

# Test list
test_list = [1, 2, 3, 4]

# Test result
test_incr_list()
```