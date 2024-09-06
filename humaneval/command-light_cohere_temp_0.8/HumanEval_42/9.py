```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l = [i+1 for i in l]
    return l[:n]

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [21, 18, 14],
    [101, 45, 66]
]

for item in test_incr_list:
    actual = incr_list(item)
    assert actual == item, "Test case {} failed.".
```