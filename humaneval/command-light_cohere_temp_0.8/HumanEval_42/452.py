```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = []
    for i in range(n):
        res.append(l[i] + 1)
    return res

# Test the function with different list inputs
test_cases = [
    [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123], [100, 2, 98, 1, 3, 97]
]

for case in test_cases:
    actual = incr_list(case)
    expected = [2, 3, 4]
    assert actual == expected, f"Test case {case} failed: {actual} != {expected}"
```

The code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The test cases ensure that the function works correctly with different list inputs.