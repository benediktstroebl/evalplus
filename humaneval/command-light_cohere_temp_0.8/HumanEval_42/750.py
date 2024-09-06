```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3] + [4]

# Test the function with a simple list
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)
assert list(result) == [6, 3, 6, 4, 6, 4, 10, 1, 124]

# Test the function with nested list
test_list = [[5, 3, 5], [2, 3, 5, 3], [9, 0, 123]]
result = incr_list(test_list)
assert list(result) == [[6, 3, 6], [4, 3, 6, 3], [4, 10, 1, 124]]
```