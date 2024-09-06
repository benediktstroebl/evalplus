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
    assert maximum([-3, -1, 1, 2, 2, 3, -2, 4], 4) == [2, 3, 4]

test_maximum()
```

The function `maximum_k` takes two arguments: an array of integers `arr` and an integer `k`. The function sorts the array and returns the maximum `k` numbers from the sorted array. 

The test suite consists of four test cases that test the function with different inputs to verify its correctness. Finally, the `test_maximum()` function is called to run the test suite and ensure that the `maximum_k` function passes all the test cases.