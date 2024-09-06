Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]

# Test Cases
print(maximum([-3, -4, 5], 3))
print(maximum([4, -4, 4], 2))
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))
```

The function `maximum_k` takes in two parameters, `arr` and `k`. The former is a list of integers and the latter is a positive integer. The function sorts the list and returns the first `k` elements, thereby ensuring that the `k` maximum numbers in the input list are returned as a list of length `k`. 

The test cases are also included to validate the function. The tests are rolled back in the output as a markdown code block:
```python
```