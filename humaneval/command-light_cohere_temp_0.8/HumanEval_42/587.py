```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

# Test the function with a list of integers
test_list = [1, 2, 3]
expected = [2, 3, 4]
result = incr_list(test_list)
assert result == expected

# Test the function with a list of strings
test_str = ["abc", "def", "int"]
expected_str = ["abc", "ef", "int"]
result_str = incr_list(test_str)
assert result_str == expected_str
```