```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test the function with a list of values
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Function call
result = incr_list(test_incr_list)

# Print the result
print(result)

# Test the function with nested list
test_nested = [[1, 2, 3], [4, 5, 6]]
result_nested = incr_list(test_nested)
print(result_nested)
```  This Python code defines a function `incr_list` that incrementally the elements of a given list by 1. It returns a value for a list comprehension with a list of integers. The test_incr_list is tested with this value. The output is a list [6, 5, 7, 4, 5, 6]. The `test_nested` variable is a nested list. It is passed to the `incr_list` function, and the result is printed.