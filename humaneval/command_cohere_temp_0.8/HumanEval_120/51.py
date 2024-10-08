Here's a Python script that includes a function `maximum_k(arr, k)` to solve the problem:
```python
def maximum_k(arr, k):
    return sorted(arr)[-k:][:k]

# Test cases
arr1 = [-3, -4, 5]
k1 = 3
print(maximum_k(arr1, k1))  # Output: [-4, -3, 5]

arr2 = [4, -4, 4]
k2 = 2
print(maximum_k(arr2, k2))  # Output: [4, 4]

arr3 = [-3, 2, 1, 2, -1, -2, 1]
k3 = 1
print(maximum_k(arr3, k3))  # Output: [2]
```

The function `maximum_k` sorts the input array and returns the last `k` elements (or the first `k` elements if the array was sorted in descending order). This approach has a time complexity of `O(k log n)` due to the sorting step, where `n` is the length of the input array.