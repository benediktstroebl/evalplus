Here's a Python script that contains a function named `maximum_k` that addresses the problem described in the markdown code block:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Test the function with examples provided in the problem statement
example1 = [-3, -4, 5], 3
expected1 = [-4, -3, 5]
test1 = maximum(*example1)
assert test1 == expected1

example2 = [4, -4, 4], 2
expected2 = [4, 4]
test2 = maximum(*example2)
assert test2 == expected2

example3 = [-3, 2, 1, 2, -1, -2, 1], 1
expected3 = [2]
test3 = maximum(*example3)
assert test3 == expected3
```

In the `maximum` function, we first sort the input array `arr`, and then return a slice of the sorted array with a length of `k` to obtain the top `k` numbers. This approach ensures the result is sorted and consists of the maximum values in the original array.