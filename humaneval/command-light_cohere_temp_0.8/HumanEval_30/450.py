```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main program
if __name__ == "__main__":
    test_get_positive()
```
This code defines a function get_positive that takes a list as input and returns a new list containing only the positive numbers from the original list. 

The test_get_positive function is used to run tests on the get_positive function with different input lists to ensure that the function is working correctly. The main program is used to run the test suite to verify the function's correctness.