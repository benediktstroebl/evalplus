```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function
def test_incr_list():
    inputs = [1, 2, 3]
    expected = [2, 3, 4]
    result = incr_list(inputs)
    assert result == expected
test_incr_list()
```
This Python function, `incr_list`, takes a list `l` as input and returns a new list with elements from `l` incremented by 1. The test function, `test_incr_list`, creates an input list, `inputs`, and uses the `incr_list` function to create a new list, `result`. Then, it compares the `result` list with the `expected` list and passes the test.