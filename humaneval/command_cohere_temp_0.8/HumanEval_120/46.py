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

The function `maximum_k` takes in an array `arr` and an integer `k` as parameters and returns a sorted list of length `k` with the maximum `k` numbers in `arr`. This is achieved by sorting the array and returning the first `k` elements. The script also includes test cases to validate the function. 

The code is encapsulated in a single self-contained function, which can be called multiple times with different arguments to solve the problem. When invoked, it returns the desired output without needing any additional code or external dependencies.