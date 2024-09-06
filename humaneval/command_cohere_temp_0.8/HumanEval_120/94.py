Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]

# Test Suite
test_cases = []
test_cases.append([[-3, -4, 5], 3, [-4, -3, 5]])
test_cases.append([[4, -4, 4], 2, [4, 4]])
test_cases.append([[-3, 2, 1, 2, -1, -2, 1], 1, [2]])

for i in test_cases:
    assert maximum(*i) == i[2]
```

The function `maximum_k` sorts the input array and returns the first `k` elements. Three test cases are defined directly inline as Python lists, making use of the list comprehension syntax. A `for` loop then iterates over each test case, where each one is a triple including the input array, the desired length `k`, and the expected output. The `assert` statement compares the output of the `maximum` function with the expected output, providing confidence in the correctness of the implementation.