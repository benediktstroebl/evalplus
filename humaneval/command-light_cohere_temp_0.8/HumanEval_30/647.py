```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([-1000, 2, -4, 5])
    assert not get_positive([5, 0, -20])
    assert not get_positive([down_for_me])  # Added a problematic element
    assert len(get_positive([1, 2, 3, -4, 5])) == 4
```