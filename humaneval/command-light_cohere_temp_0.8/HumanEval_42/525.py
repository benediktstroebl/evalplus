```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [10, 20, 30, 40]
]

for i, test in enumerate(test_cases):
    actual = incr_list(test)
    expected = test
    assert actual == expected, f"Test {i+1}: {actual} != {expected}"
```
The code defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The function uses a generator expression `[x + 1 for x in l]` to achieve this, and the result is returned. The code also provides a test cases, and uses the assert statement to check if the `incr_list` function returns the correct result for each test case.