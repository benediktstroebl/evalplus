```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 9
    assert get_positive([2, -2, 3, -3, 4, -4, 5]) == [2, 3, 4]
    assert get_positive([1, 2, 3, 4, -3, 5, 6]) == [1, 2, 3, 4]

if __name__ == "__main__":
    test_get_positive()
```
This code defines a function `get_positive` that filters out negative numbers from an input list and returns a new list containing only the positive numbers. The function is then tested with a series of test cases using the `test_get_positive` function, which asserts that the function's behavior matches the specified conditions.