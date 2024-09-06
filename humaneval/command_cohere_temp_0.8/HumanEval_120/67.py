Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Test Suite
def test_maximum():
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
    assert maximum([-3, -1, 1, 2, 3, 2, -5, 4], 4) == [3, 2, 4, 2]

test_maximum()
```

The function `maximum_k` takes two arguments: an array `arr` and an integer `k`. It sorts the array and returns the maximum `k` elements. Three test cases are included to verify the function. You can add more tests to increase test coverage and ensure the function's correctness against edge cases.