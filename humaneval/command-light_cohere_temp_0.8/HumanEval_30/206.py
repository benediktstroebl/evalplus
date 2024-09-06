```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([55, 33, 11, 33,99])) == 4
    assert get_positive([8, 88, 333]) == [88, 333]
    assert get_positive([9, -4, 3, -20]) == [9, 3]
    assert get_positive([15, -200, -15]) == [-15, -200]
```