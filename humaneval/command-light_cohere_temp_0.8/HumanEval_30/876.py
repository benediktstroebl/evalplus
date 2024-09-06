```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 7
    assert get_positive([9, 8, 7, 6, 5]) == [9, 8, 7]
    assert get_positive([-2000, 3, 4, -5]) == [3, 4, 5]

if __name__ == "__main__":
    test_get_positive()
``` 
The code defines a function `get_positive` that takes in a list and returns a new list with only the positive integers from the original list. The test suite then tests the single function with various input scenarios, and the expected output is validated against the actual result of the `get_positive` function.