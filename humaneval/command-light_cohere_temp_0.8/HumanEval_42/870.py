```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [x + 1 for x in l]
    return l

# Test the function with a list of lists
test_incr_list = [[1, 2, 3], [5, 3, 5], [2, 3, 3]]
result = incr_list(test_incr_list)

# Print the result
print(result)
```