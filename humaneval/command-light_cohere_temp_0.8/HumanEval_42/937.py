```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    result[0] = l[0]
    for i in range(1, n + 1):
        result[i] = l[i - 1] + 1
    return result

# Test the function with sample inputs
test_incr_list = incr_list([1, 2, 3])
print("Test 1: ", test_incr_list)  # Output: [2, 3, 4]
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 2: ", test_incr_list)  # Output: [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
test_incr_list = incr_list([])  # Empty list
print("Test 3: ", test_incr_list)  # Output: []
```