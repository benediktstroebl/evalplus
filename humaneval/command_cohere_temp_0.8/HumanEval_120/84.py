Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]

# Test cases
print(maximum([-3, -4, 5], 3))
print(maximum([4, -4, 4], 2))
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))
```

The function `maximum` takes in an array `arr` and an integer `k` as parameters and returns a sorted list of the maximum `k` numbers in `arr`. This is achieved by sorting the array and returning the first `k` elements. The number of tests could be increased to test the efficiency of the solution.