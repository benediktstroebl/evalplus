```python
def sort_array(array):
    odd, even = sorted(array), sorted(array, reverse=True)
    return odd if sum(array[0], array[-1]) % 2 else even
```

The script uses basic conditional logic to sort the array and then returns the sorted array based on the condition specified in the problem. It sorts the array in ascending order if the sum of the first and last index values is odd, and it sorts the array in descending order if the sum of the first and last index values is even. The `sorted()` function is used to sort the array, and the `reverse` parameter is set to `True` to sort the array in descending order. Finally, the sorted array is returned based on the specified condition.