```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(x + 1 == result[i] for i, x in enumerate(l))
    return result

# Test the function with a range of inputs
for i in range(10):
    assert incr_list([i]) == [i + 1]
```