```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, the lambda function `lambda x: (-bin(x).count('1'), x)` is used. 

First, the lambda function converts the element `x` to a binary string using `bin(x)`. It then counts the number of occurrences of '1' in this binary representation using `bin(x).count('1')`. This value is sorted in descending order, so the element with the most ones will sort first. 

In the event of a tie (same number of ones), the lambda function will fallback to sorting based on the element's decimal value as specified in the problem statement. 

This solution efficiently implements the specified sorting requirement in a single function, making it both concise and effective for the given problem.