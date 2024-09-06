```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with a list of elements with increment
test_incr_list = incr_list([1, 2, 3])
print("Test 1:", test_incr_list)  # Output: [2, 3, 4]
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 2:", test_incr_list)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

The Python script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements incremented by 1. The `test_incr_list` function is then called to test the function, and the results are printed to the console.