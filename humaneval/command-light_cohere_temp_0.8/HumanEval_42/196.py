```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test the function with a list of numbers
test_incr_list = incr_list([1, 2, 3])
print("Test 1: ", test_incr_list)  # Output: [2, 3, 4]

test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 2: ", test_incr_list)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Add some edge cases
test_incr_list = incr_list([])  # empty list
test_incr_list = incr_list([9, 2, 1])  # [2, 1]
test_incr_list = incr_list([[2, 3, 4, 5], 6])  # [2, 3, 4, 5]

# Output:
print("Test 3: ", test_incr_list)  # Output: [2, 3, 4, 5]
print("Test 4: ", test_incr_list)  # Output: [9, 3, 2, 1]
```