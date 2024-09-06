```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. If the sum is odd, the array is sorted in ascending order using the `sorted()` function. If the sum is even, the array is sorted in descending order by setting the `reverse` parameter of the `sorted()` function to `True`. Finally, the sorted array is returned as a copy of the original array. 

This approach ensures correctness while maintaining efficiency by utilizing the built-in sorting functionality provided by Python's `sorted()` function.