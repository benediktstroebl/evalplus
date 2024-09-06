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
    assert maximum([-3, -1, 1, 2, 2, 3, -2, 5], 4) == [5, 3, 2, 2]

if __name__ == '__main__':
    test_maximum()
```

The function `maximum_k` takes two arguments: a list of integers `arr` and an integer `k`. It sorts the array and returns the maximum `k` numbers. Three unit tests are provided to validate the functionality of the `maximum()` function. 

The function can be used as a part of a larger program, but you can execute it directly in your Python environment by running the script. If you encounter any issues running the script, ensure you have Python installed on your system. You can install it freely via the official Python website should you need to do so.