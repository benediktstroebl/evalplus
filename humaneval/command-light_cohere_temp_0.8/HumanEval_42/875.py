```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_elements = [x + 1 for x in l]
    return new_elements

# Test case 1: Basic increment
test_incr_list = [1, 2, 3]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test case 2: Remove first element and increment
test_incr_list = [5, 3, 5, 2, 3, 3]
result = incr_list(test_incr_list)
assert result == [6, 4, 6, 3, 4]

# Test case 3: Multiple increment by 2
test_incr_list = [5, 3, 5, 2, 3, 3]
result = incr_list(test_incr_list)
assert result == [8, 5, 7, 4, 6]

# Test case 4: List with 0
test_incr_list = [0, 5, 3, 2, 3, 3]
result = incr_list(test_incr_list)
assert result == [2, 3, 4]

# Test case 5: List with 123
test_incr_list = [5, 3, 5, 2, 3, 3, 123]
result = incr_list(test_incr_list)
assert result == [7, 5, 7, 4, 6]

# Test case 6: Dictionary test
test_incr_dict = {'a': 1, 'b': 2, 'c': 3}
result = [x + 1 for x in test_incr_dict.items()]
 assert result == [2, 3, 4]
```

This Python script defines a function `incr_list` that creates a new list by incrementing elements of the input list by 1. It also includes several test cases to verify the functionality of the `incr_list` function. 
The output of the script will be the list with elements incremented according to the test cases.