```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 9
    assert get_positive([0]) == []
    assert get_positive([20, 30, 40, -20]) == [20, 30, 40]

# Main program point
if __name__ == "__main__":
    test_get_positive()
```
This code provides a self-contained function get_positive that takes in a list and returns a new list with only the positive numbers. It also has a test suite to check the correctness of the get_positive function against a set of test cases. This script is single program point, which will execute the test suite and the function get_positive.