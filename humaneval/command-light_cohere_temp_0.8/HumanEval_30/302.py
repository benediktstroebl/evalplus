```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([5, 0, -20])  # 0 should be excluded
    assert not get_positive([-100, -200, -1])  # Negative numbers should be skipped
    assert get_positive([1, 2, -3, -4, -5]) == [1, 2, -3, -4]
test_get_positive()
```
This script defines a function get_positive that filters a given list to include only positive numbers. It also includes a tests the simple test cases for the function to ensure its correctness.