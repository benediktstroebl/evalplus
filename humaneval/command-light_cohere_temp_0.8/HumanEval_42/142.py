```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]

# Test the function with various inputs
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 5])
test_incr_list.append([5, 4, 6])

# Verify the expected output using the function
result = incr_list(test_incr_list)

print("Result:", result)
```