```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that will be used to transform each element of the list before sorting. Here, a lambda function `lambda x: (bin(x).count('1'), x)` is used. This function first converts the elements to their binary representation using the `bin` function, counts the number of occurrences of '1' in each binary representation using the `count` method, and returns this count together with the element itself. The `sort` function then sorts the array based on these returned values.

The code successfully sorts the given arrays according to the specified criteria and meets the expectations outlined in the task. You can verify this by running the code with the example inputs provided in the task, ensuring that it returns the expected sorted arrays for each case.