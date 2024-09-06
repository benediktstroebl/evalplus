```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function
def test_get_positive():
    assert get_positive([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
    assert get_positive([-1, -5, 6, 7]) == [1, 5, 6]
    assert get_positive([0, 0, 00, 00]) == [0]
    assert get_positive([]) == []
    assert get_positive([4, -4]) == [4]
    assert get_positive([1, 2, 3, -1]) == [1, 2, 3]

# Driver code
test_get_positive()
```
The provided code defines a function `get_positive` that takes an input list and returns a new list with only the positive elements. It also contains a test_get_positive, which verifies the correctness of the `get_positive` function using a variety of test cases.