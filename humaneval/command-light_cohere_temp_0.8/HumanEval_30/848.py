```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test cases
tests = [
    """Input: [-1, 2, -4, 5, 6]
    Expected Output: [2, 5, 6]
    """
    return get_positive([-1, 2, -4, 5, 6])

# Test cases: valid input
tests2 = [
    """Input: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    Expected Output: [5, 3, 2, 3, 9, 123]
    """
    return get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
]

# Run the tests
for test in tests:
    assert test() == tests2[test]
``` 
The function get_positive takes a list of numbers as input and returns a new list containing only the positive numbers. The tests are a separate set of test cases that pass this function and verify that it works correctly with various inputs.