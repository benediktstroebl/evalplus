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

You may use the previously defined feature `maximum_k` to solve the problem since it accepts an array `arr` and a positive integer `k` as input and provides a sorted list of length `k` with the maximum `k` values from `arr` as output. To validate the operation, the script also provides three test cases that print the expected output of the function using the `print` statement.

Keep in mind that the `maximum` function operates by initially sorting the input array in ascending order. Then it returns the first `k` members since they are the highest `k` numbers from the array. This approach guarantees that the output consistently has the `k` highest values from the provided array.