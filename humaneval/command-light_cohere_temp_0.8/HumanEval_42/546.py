```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x + 1 for x in l] + [n]
    return res

# Test the function with a list of elements in a markdown code block
# Test the incr_list function with a list ([5, 3, 5, 2, 3, 3, 9, 0, 123])
# Should return: [6, 3, 6, 4, 6, 4, 10, 1, 124]
# Test the incr_list function with a list of strings, to demonstrate flexibility
# Test the incr_list function with a list ([0, 1, 2, 3, 4, 5])
# Should return: [1, 2, 3, 5, 6]
```