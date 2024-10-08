```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` sorts the array based on the sum of the first and last elements in the array. If the sum is odd, it sorts the array in ascending order using the `sorted()` function. If the sum is even, it sorts the array in descending order by setting the `reverse` parameter in the `sorted()` function to `True`. The mutations of the original array are done using the `array[:] = ...` syntax, which modifies the original array.