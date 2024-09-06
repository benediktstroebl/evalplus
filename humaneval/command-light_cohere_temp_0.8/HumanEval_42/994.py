```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l] + [n]
    assert len(result) == len(l) + 1, f"Input list and result are of different lengths: {len(l)}, {len(result)}"
    return result

# Test the function with a sample input
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_golden = [6, 3, 6, 4, 6, 4, 10, 1, 124]
assert result_golden == incr_list(input_list), "Function did not return expected output."
```