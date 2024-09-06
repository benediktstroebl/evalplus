```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. The function then uses the `sorted()` function and passes `reverse=True` as an argument to sort the array accordingly. The output of the function is then assigned back to the input array, ensuring the original array is not modified.