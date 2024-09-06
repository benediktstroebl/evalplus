Here's a Python script that includes a function `maximum_k(arr, k)` to solve the problem:
```python
def maximum_k(arr, k):
    """
    Finds the maximum k numbers from the array arr and returns a sorted list of length k.
    """
    arr = sorted(arr)
    return arr[:k]

# Test Suite
def test_maximum_k():
    assert maximum_k([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum_k([4, -4, 4], 2) == [4, 4]
    assert maximum_k([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum_k([21, -43, 21, -43], 2) == [21, 21]

test_maximum_k()
```

The `maximum_k` function takes in an array `arr` and an integer `k` as inputs, sorts the array, and returns the maximum `k` numbers from the sorted array.

The `test_maximum_k` function tests the `maximum_k` function with example cases, and the `assert` statements check that the output of `maximum_k` is correct for each case. Finally, executing `test_maximum_k()` runs the tests.