```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

#Test cases
test_incr_list = [
    [
        ( [1, 2, 3], [2, 3, 4]), 
        ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1])
    ]
]

# Function calls and results
for t, expected in test_incr_list:
    actual = incr_list(t)
    assert actual == expected
```