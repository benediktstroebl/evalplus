```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic function call
test_case1 = incr_list([1, 2, 3])
print("Test Case 1: ", test_case1)

# Test case 2: List with repeated values
test_case2 = incr_list([5, 3, 5, 2, 3, 3])
print("Test Case 2: ", test_case2)

# Test case 3: List with zero values
test_case3 = incr_list([9, 0, 123])
print("Test Case 3: ", test_case3)

# Test case 4: Complex list
test_case4 = incr_list([6, 4, 6, 3, 4, 6])
print("Test Case 4: ", test_case4)
```

The code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The `test_cases` list contains several test cases, and each test case is passed to the `incr_list` function to create a new list and then print the result.