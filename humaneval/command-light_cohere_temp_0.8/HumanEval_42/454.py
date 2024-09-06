```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test cases
test_incr_list = [
    [
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ]
]

for test in test_incr_list:
    assert list(incr_list(test)) == test, "Test {} failed".
```