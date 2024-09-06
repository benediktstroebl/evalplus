```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test the function with a list of integers
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
# Check if the result matches the expected output
if list(result) != test_incr_list:
    raise ValueError("Incorrect result!")
```