```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l] + [n]
    assert len(result) == len(l) + 1, "Length mismatch"
    assert all(result[i] == i + 1 for i in range(len(l))), "Inconsistent increment"
    return result

# Test the function
test_incr_list = incr_list([1, 2, 3])
print(test_incr_list)
```