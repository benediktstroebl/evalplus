```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    return result

# Test cases
test_incr_list = [
    [
        (1, [1]),
        (2, [2, 3]),
        (3, [5, 3, 5, 2, 3])
    ], [
        [2, 3],
        [6, 4],
        [10, 7]
    ])
]

# Execute test cases
for test in test_incr_list:
    assert incr_list(test[1]) == test[2]
```