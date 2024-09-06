```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n, f"Length mismatch: Got {len(result)}, Expected {n}"
    assert all(i >= n-1 for i in result), f"Inconsistent index: Got {result}, Expected sorted list"
    return result

# Test the function
# Test with a list of numbers
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_list)
print(test_result)  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test with list of strings
test_str = ["Python", "Am, i", "cant", " recover"]
test_result = incr_list(test_str)
print(test_result)  # Expected output: ["7, 5, 7, 6, 4, 4, 12"]
```