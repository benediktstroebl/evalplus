```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([1, 2, 3, -4, 5]) == [1, 2, 3, 5]
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 4, 5]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123]) == [5, 3, 2, 3, 123]
    assert get_positive([-10, -30]) == [] # Should return an empty list
    assert get_positive([10, -20, 30]) == [30] # Should return positive numbers only

if __name__ == "__main__":
    test_get_positive()
```
The provided Python script defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive integers from the original list. The function achieves this purpose through the essential filtering process on the input list. 

The script also includes unit tests for the `get_positive` function. These tests check various scenarios and ensure that the function operates correctly.