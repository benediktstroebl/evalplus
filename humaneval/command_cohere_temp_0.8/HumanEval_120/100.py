Here's a Python script that contains a function to solve the problem and example tests to verify its correctness:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Test cases
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

The `maximum` function takes in an array `arr` and an integer `k` as inputs, sorts the array, and then returns the first `k` elements. The test cases are included to validate the function's behavior against the expected output. Adjusted spacing and indentation for clarity.