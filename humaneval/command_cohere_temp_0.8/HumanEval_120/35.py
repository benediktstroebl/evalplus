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
    assert maximum([1, 3, 2, 4, -3, 2, 0, -1], 4) == [4, 3, 2, 2]

test_maximum()
```

The function `maximum_k` takes two parameters, a list of integers `arr` and an integer `k`. The function sorts the array and returns the maximum k numbers from the sorted array.

The test suite consists of four test cases that test the function with various inputs to validate its correctness.

You can execute this code to see if the tests pass to confirm the functionality of the `maximum_k` function. Let me know if you have any questions!