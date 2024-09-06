```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.push([
    [ [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] ])

# Function test
def test_function():
    assert get_positive([]) == []
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert get_positive([]) == []
    assert get_positive([7, -7]) == []
    assert get_positive([3, -9, 7, -10, 90]) == [3, 7, 90]

# Run the test suite
test_get_positive
```
This script defines a function `get_positive` that filters out any negative numbers from an input list and returns a new list with the positive values. The test suite tests the both simple cases and edge cases to ensure that the function behaves as expected.