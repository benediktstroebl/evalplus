```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [i+1 for i in l]
    return l

# Test with given input
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_list)
print(test_result)  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This code defines a function, incr_list, which takes a list l as input and returns a new list with elements from input list l incremented by 1. The code also tests thecolizes the list and returns the result.