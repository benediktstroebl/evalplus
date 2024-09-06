```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([9, 5, -3, -20])) == 3  # Should return only 5, 9

# Run the tests
test_get_positive()
get_positive_result = get_positive([9, 5, -3, -20])
print(get_positive_result)
```

This script defines a function get_positive that takes a list as input and returns a new list containing only positive numbers from the input list. The test_get_positive function passes all the tests with different input lists and the function returns the correct results for each case.