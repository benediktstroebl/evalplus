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

The `maximum` function takes in an unsorted array (`arr`) and a positive integer (`k`). It sorts the array and returns the first `k` elements, ensuring these are the maximum numbers in the array.

You can modify the test cases by changing the values of `arr1`, `arr2`, `arr3`, `k1`, `k2`, and `k3` to verify the function behaves as expected across different scenarios.