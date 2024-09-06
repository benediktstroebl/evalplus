```python
def unique(lst):
    return list(set(lst))

# Test suite for unique function
def test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Driver code to run the test suite
test()
``` 
This script defines a function named unique that takes a list as an argument and returns a new list containing only the unique elements from the original list using the set() and list() constructor. The test suite contains a test function, which passes the test using the unique() function with a known input list. 
Finally, the main driver code runs the test suite, which checks that the function is working as expected.