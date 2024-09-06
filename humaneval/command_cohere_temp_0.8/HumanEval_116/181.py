```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that does custom sorting. In this case, for every element `x` in the array, the lambda function returns a tuple of `bin(x).count('1')` and `x`, the number of ones in the binary representation and the decimal value of `x`, respectively. The elements are then sorted based on this 2-tuple in ascending order.

This method has a time complexity of O(log n) due to the call to `bin` and `count` and an auxiliary space complexity of O(1) since it only does sorting in-place and doesn't allocate any additional memory.

The tests proposed in the problem specification are covered by the provided function, and the result of each test case is as expected.

This approach provides an efficient and concise solution to the problem.