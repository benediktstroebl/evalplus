```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [n+1] * (n+1)
    return l

# Test cases
test_incr_list = [
    [
        [1, 2, 3], 
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ]
]

for item in test_incr_list:
    assert list(incr_list(item)) == item, f"Failed for {item}."
```