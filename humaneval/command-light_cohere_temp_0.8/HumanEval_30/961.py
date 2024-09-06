```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert len(get_positive([55, 33, 11, 99])) == 3
    assert get_positive([19, 20, 21]) == [19, 20]
    assert get_positive([19, 20, 22]) == [19, 20, 22]

# main code
if __name__ == "__main__":
    test_get_positive()
```