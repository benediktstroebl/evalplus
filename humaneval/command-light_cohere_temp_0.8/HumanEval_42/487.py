```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in range(n)]
    return result

# Test the function with various lists and checks the returned values
def test_incr_list():
    # Create various lists
    test_lists = [1, 2, 3, [4, 5], [6, 7], [8, 9, 10]]
    # Test different cases
    for test_list in test_lists:
        actual = incr_list(test_list)
        expected = [i+1 for i in test_list]
        assert actual == expected, f"Test case {test_list} failed"

# Run the test suite
test_incr_list()
``` 
This code defines a function incr_list that returns a list with elements incremented by 1. The function is then tested with various input lists using the test_incr_list function. The test suite checks if the result matches the expected list for each input.