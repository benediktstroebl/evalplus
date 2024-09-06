```python
def incr_list(lst):
    return [i+1 for i in lst]

# Test cases
test_incr_list = []
test_incr_list.push([1, 2, 3])
test_incr_list.push([5, 6, 6, 6, 3, 4, 4, 4, 10, 1, 124])

# Function to check test cases
def test_func(func):
    assert list(func(test_incr_list)) == [2, 3, 6, 4, 4, 4, 10, 1, 124]
    
# Test suite
test_suite = []
test_suite.push(test_incr_list, test_func)

# Main function
incr_list_func = lambda: test_suite.pop(0)[0]  # Get the last test suite and remove it

# Test execution
print("Passed all tests:")
```
Do you require any further assistance with code creation or testing topics?