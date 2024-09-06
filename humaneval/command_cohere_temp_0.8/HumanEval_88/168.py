```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` sorts the array based on the sum of the first and last elements, if the sum is odd, it sorts the array in ascending order using the `sorted()` function, and if the sum is even, it sorts the array in descending order using the `sorted()` function with the `reverse=True` argument.