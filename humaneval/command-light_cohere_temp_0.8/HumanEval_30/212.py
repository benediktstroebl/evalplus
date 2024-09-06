```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert len(get_positive([1, 2, -3, -100])) == 3   # Should return only [-100]
    assert len(get_positive([1, 2, 3, -100])) == 1    # Should return only [-100]
    assert get_positive([]) == []
```