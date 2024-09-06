```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + [n]
    assert len(result) == len(l) + 1
    assert all([i+1 == result[i] for i in range(len(l))])
    return result

# Test the function
# with known inputs
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_data)
print(test_result)
```