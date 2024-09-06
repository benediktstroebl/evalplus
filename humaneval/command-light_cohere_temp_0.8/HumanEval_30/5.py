```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([-1, 2, -4, 5, 6, 7])
    assert not get_positive([9, 8, 3, -200, -100])

if __name__ == "__main__":
    test_get_positive()
```
The code defines a function `get_positive` that filters a list for only positive numbers. The test suite `test_get_positive` is used to check the correctness of this function by providing a variety of test cases and assertions.