```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test cases
test_incr_list = [
    ( [1, 2, 3], ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123],),
    ([10, 11, 12],)
]

for test, expected in test_incr_list:
    actual = incr_list(test)
    print(f"Test: {test}, Expected: {expected}, Actual: {actual}")
```