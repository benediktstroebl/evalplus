```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test cases
test_incr_list = [
    ( [1, 2, 3], [2, 3, 4 ] ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
]

# Function call and results
for case in test_incr_list:
    lst = incr_list(case[0])
    assert lst == case[1]
```