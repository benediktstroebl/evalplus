```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test cases for the function
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 4, 8, 3, 3]
]

# Function call and assertions
assert list(incr_list(test_incr_list)) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Failed to increment elements correctly."
```