```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([5, 3, -5, -100, 2, -3, 3, 9, 0, 123, 1])
    assert not get_positive([])
    assert not get_positive([None])
    return True

# main
if __name__ == "__main__":
    test_get_positive()
```

This code defines a `get_positive` function that takes a list as input and returns a new list with only the positive elements. The function utilizes a loop to iterate through each element of the input list and compares each element with the `>= 0` condition. The test suite includes several test cases to verify the correctness of the `get_positive` function, passing various lists and conditions.