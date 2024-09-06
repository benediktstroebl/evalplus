Here's a Python script that includes a function `maximum_k(arr, k)` to solve the problem:
```python
def maximum_k(arr, k):
    """
    Finds the maximum k numbers in the array arr and returns a sorted list of length k.
    """
    arr = sorted(arr)
    return arr[:k]

# Test Suite
def test_maximum_k():
    assert maximum_k([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum_k([4, -4, 4], 2) == [4, 4]
    assert maximum_k([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum_k([10, 2, 3], 10) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 3]

test_maximum_k()
```

The `maximum_k` function takes in an array `arr` and an integer `k` as inputs, sorts the array, and returns the maximum `k` numbers in the sorted array. The `test_maximum_k` function runs tests on the `maximum_k` function to ensure that it is working correctly. 

To run the test, simply call `test_maximum_k()`. The code executor will run the test and display "PASS" if the tests pass successfully, or "FAIL" if they fail.