```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test the function with a list with specified elements
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]

# Function call with test list
result = incr_list(test_incr_list)

# Compare the result with the expected output
print("Result:", result)
print("Expected:", [6, 4, 6, 3, 4, 4, 10, 1, 124])
```