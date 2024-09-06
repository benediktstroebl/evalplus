```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test the function
def test_incr_list():
    # Test list with odd elements
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(lst)
    assert result == expected, "Expected and actual are not equal"

# Test the function with a list of numbers
lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(lst)
assert result == expected, "Expected and actual are not equal"

# Test the function with a mix of numbers and strings
lst = ["abc", 5, "hello", 3, "world"]
expected = ["abc", 6, "hello", 3, "world"]
result = incr_list(lst)
assert result == expected, "Expected and actual are not equal"

test_incr_list()
```
The above Python script defines a function `incr_list` that increments each element in a given list by 1 and tests the function with various inputs using `test_incr_list` function.  The test suite of test cases, which cover scenarios with both numbers and strings in the input list.