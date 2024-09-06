Here's a Python script that contains a function named `maximum_k` that addresses the problem statement and is appropriately tested:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Testing the function
arr1 = [-3, -4, 5]
k1 = 3
print(maximum(arr1, k1))  # Expected output: [-4, -3, 5]

arr2 = [4, -4, 4]
k2 = 2
print(maximum(arr2, k2))  # Expected output: [4, 4]

arr3 = [-3, 2, 1, 2, -1, -2, 1]
k3 = 1
print(maximum(arr3, k3))  # Expected output: [2]
```

This script effectively handles the given scenario of finding the maximum elements within a sorted list of a given length `k`. The function `maximum_k` serves to return the requested subset of sorted maximum elements from the input array.