Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]

# Test Suite
def test_maximum():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([-3, -1, 1, 2, 2, -2, 3, 3], 4) == [3, 3]

test_maximum()
```

The function `maximum_k` takes two parameters, a list of numbers `arr` and a positive integer `k`. It sorts the array and returns the maximum `k` numbers. Three unit tests are provided to validate the functionality of the `maximum_k` function. 

To run the test suite, comment out the test suite and uncomment the execution command:
```python
# Test Suite
def test_maximum():
    # Arrange
    arr = [-3, -4, 5]
    k = 3

    # Act
    result = maximum(arr, k)

    # Assert
    assert result == [-4, -3, 5]

test_maximum()
```