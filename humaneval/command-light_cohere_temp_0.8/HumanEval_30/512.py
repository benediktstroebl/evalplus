```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([9, 7, 5, 1, 3])) == 3
    assert get_positive([19, 2, 13]) == [19, 2]
    assert get_positive([123, -4, -23]) == [123]
    assert get_positive([-33, -5, -1, -9, -77]) == [-77]
```