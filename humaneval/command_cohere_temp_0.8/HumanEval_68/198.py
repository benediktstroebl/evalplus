Here's a Python script that solves the given problem with an efficient algorithm using a `min` function and a `filter` function to find the smallest even value in the array and its index:
```python
def pluck(arr):
    even_values = filter(lambda x: x % 2 == 0, arr)
    min_value = min(even_values)
    min_index = min(idx for idx, value in enumerate(even_values) if value == min_value)
    
    return [min_value, min_index] if min_value else []
```

The function leverages Python's built-in `min` function and `filter` function to efficiently find the smallest even value and its index in the array. The `filter` function is used to extract even values from the input array, and then the `min` function is used to find the smallest even value along with its index using a generator expression.

This solution has a time complexity of O(E) where E is the number of even values in the array, which can be charged as O(N) because it runs through the array once to find the smallest value and then again for index finding, assuming the array is sorted or shuffled.