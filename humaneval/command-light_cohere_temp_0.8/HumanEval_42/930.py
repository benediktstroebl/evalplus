```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [2, 3]

# Test the function with a list of elements
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)

# Print the result
print(result)
```