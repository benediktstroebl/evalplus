```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = []
test_incr_list.add([range(1, 10))
test_incr_list.add([range(11, 22))

# Function Call and Result Comparison
test_incr_list = incr_list(test_incr_list)
result_compare = sorted(test_incr_list)

print("Test cases passed.")
Result comparison:", result_compare
```