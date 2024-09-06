```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [l[-1] + 1]
    return l

# Test cases
test_incr_list = [
    (
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
     # ([1, 2, 3, 4], [5, 6, 7, 8, 9, 10])
    ),
]

for item, expected in test_incr_list:
    actual = incr_list(item)
    print(f"Test {item}: {actual}, expected={expected}")
    assert actual == expected
```