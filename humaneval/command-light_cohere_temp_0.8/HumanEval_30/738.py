```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([9, 5, -5])
    assert not get_positive([5, -5, 3, -3])

if __name__ == "__main__":
    test_get_positive()
```
This code defines the function **get_positive**, which takes a list as input and returns a new list containing only the positive elements from the original list. The test suite at the