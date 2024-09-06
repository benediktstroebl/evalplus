```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test the function with sample inputs
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 4])
test_incr_list.append([5, 4, 5])
test_incr_list.append([5, 3, 5])
test_incr_list.append([6, 3, 5])
test_incr_list.append([1, 2, 3])

def test_func(test_list):
    """Function to test if a given list is a valid input for incr_list function."""
    test_incr_list = incr_list(test_list)
    return test_incr_list == test_list

# Call the function with the test inputs
result = test_func(test_incr_list)

# Print the result
print(result)
```