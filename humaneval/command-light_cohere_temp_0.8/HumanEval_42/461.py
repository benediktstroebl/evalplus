```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n+1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with a range of lists
test_lists = [
    [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123], [1]
]

for test_list in test_lists:
    actual = incr_list(test_list)
    expected = [2, 3, 4]
    assert actual == expected, "List should be incremented by 1"
```