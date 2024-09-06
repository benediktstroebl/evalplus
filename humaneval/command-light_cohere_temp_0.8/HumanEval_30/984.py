```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([10, -5, -20])) == 3  # Should return [-20, -5, 10]
    assert len(get_positive([1, 2, -5, -20, 30, 40, -100])) == 4  # Should return [1, 2, -20, 30]
```