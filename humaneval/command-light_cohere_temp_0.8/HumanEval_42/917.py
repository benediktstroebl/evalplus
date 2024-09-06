```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x+1 for x in l]

# Test cases
test_incr_list = [
    ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123])
]

# Function call and results
for test in test_incr_list:
    assert list(incr_list(test)) == test
```