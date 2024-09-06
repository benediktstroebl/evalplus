```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    assert len(result) == n
    assert all(result[i] == i+1 for i in range(n))
    return result
# Example usage:
# Test with list of integers
input_list = [5, 3, 5, 2, 3, 3]
result_expected = [6, 4, 6, 3, 4, 4]
result = incr_list(input_list)
assert result == result_expected, "Error in incr_list function"
# Test with list of strings
input_str = ["hello", "world"]
result_expected_str = ["hey", "wool"]
result_str = incr_list(input_str)
assert result_str == result_expected_str, "Error in incr_list function with strings"
```

The `incr_list` function takes a list `l` as input and returns a new list with elements incremented by 1. It uses a new list comprehension with a list generator expression `(i+1)` to create the new list. The test cases cover scenarios where the list contains integers and strings, and it verifies the expected output using the `assert` assertion.