```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + [n+1]
    return result

# Test cases
test_incr_list = [
    ( [1, 2, 3], [2, 3, 4 ] ),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124])
]

# Function calls
for test in test_incr_list:
    actual_result = incr_list(test)
    print(f"Expected: { [6, 4, 6, 3, 4, 4, 10, 1, 124]} but got: {actual_result}")
```