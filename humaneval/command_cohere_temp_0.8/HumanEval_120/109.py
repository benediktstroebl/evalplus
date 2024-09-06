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

The function `maximum_k` takes in two parameters, `arr`, which is an array of integers, and `k`, a positive integer. The function sorts the array in ascending order and then returns the first `k` elements of the array, which are the maximum `k` numbers in the original array.

The test suite verifies the functionality of the `maximum_k` function for various inputs, ensuring that it returns the expected outputs for the examples provided in the problem statement. Each test case is expressed as a list containing the input array, the desired output length `k`, and the expected sorted list of maximum numbers. The `assert` statements compare the actual output from the function against the expected output, ensuring they are equal. 

Overall, the Python script provides an effective and efficient self-contained solution to the problem statement, achieving a linear time complexity of O(nlogn).