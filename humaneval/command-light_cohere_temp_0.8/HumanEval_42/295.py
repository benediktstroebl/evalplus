```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] = l[i] + 1
    return l

# Test the function
tests = [
    ( [1, 2, 3], ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], ),
    ([10, 100, 101],)
]

for test in tests:
    result = incr_list(test)
    expected = test[1]
    print(f"Test case: {result, expected}")
    assert result == expected
```
The provided Python function `incr_list` takes a list `l` as an argument and returns a new list with elements incremented by 1. The test cases provided are executed using this function, with the expected results matched against the actual results.