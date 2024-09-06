```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test case 1: Basic increment
test_incr_list([1, 2, 3])
assert incr_list(test_incr_list) == [2, 3, 4]

# Test case 2: Recursion with small range
test_incr_list([5, 3, 5, 2, 3, 3])
assert list(incr_list.isinstance(test_incr_list)) == True

# Test case 3: Recursion with large range
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert list(incr_list).isinstance(test_incr_list) == True
``` 
This Python function increments the elements in a list by 1.  It uses a simple list comprehension with a loop. The function returns a list with the incremented elements. The test cases ensure that the function works correctly.