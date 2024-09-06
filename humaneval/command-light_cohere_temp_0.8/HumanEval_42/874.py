```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with some inputs
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
test_result = [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Print the results
print("Test input:", test_list)
print("Test result:", result)
```
This code defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The function uses a list comprehension to achieve this. Then, it's tested with the given test_list and the results are printed.