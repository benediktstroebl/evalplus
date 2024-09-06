```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test cases
test_incr_list = [
    (
        [1, 2, 3],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ),
    ([10, 20, 30],),
    ([-, -5, -10, -20],),
]

# Function call and tests results
for case in test_incr_list:
    print(incr_list(case)))

# Output expected:
[[2, 3, 4], [6, 7, 8], [12, 22, 31]]
```